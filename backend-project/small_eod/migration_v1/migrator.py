import logging
from datetime import datetime
from uuid import uuid4

from pytz import timezone
from django.contrib.auth import get_user_model
from django.db import transaction

from . import models as models_v1
from ..tags.models import Tag
from ..institutions.models import Institution
from ..cases.models import Case
from ..features.models import Feature, FeatureOption
from ..channels.models import Channel
from ..letters.models import DocumentType, Letter
from ..files.models import File

logger = logging.getLogger(__name__)
MIGRATION_DB = "migration"
V2_DB = "default"


class PkMappings:
    """ Cache old_pk -> new_pk mapping when it is inconvenient to make a query """

    institution = dict()
    case = dict()
    user = dict()


def fix_timestamps(new, old):
    """ Migrate data to auto-filling timestamp fields """
    model = type(new)
    # Queryset update will ignore auto_now/auto_now_add
    model.objects.filter(pk=new.pk).update(
        modified_on=old.modified, created_on=old.created
    )
    assert_timestamps(new, old)


def assert_timestamps(new, old):
    new.refresh_from_db()
    assert new.modified_on == old.modified
    assert new.created_on == old.created


def migrate_tags():
    for old_tag in models_v1.Tag.objects.using(MIGRATION_DB).all():
        migrate_tag(old_tag)


def migrate_tag(old_tag):
    logger.debug("Migrating Tag: %s", old_tag.name)
    try:
        return Tag.objects.get(name=old_tag.name)
    except Tag.DoesNotExist:
        new_tag = Tag(name=old_tag.name)
        new_tag.save()
        return new_tag
    except Tag.MultipleObjectsReturned:
        raise RuntimeError("Data duplication detected")


def migrate_institutions():
    for old_institution in models_v1.Institution.objects.using(MIGRATION_DB).all():
        migrate_institution(old_institution)


def migrate_institution(old_institution):
    logger.debug("Migrating Institution: %s", old_institution.name)
    if old_institution.pk in PkMappings.institution:
        new_pk = PkMappings.institution[old_institution.pk]
        logger.debug("Using cached Institution with pk == %a", new_pk)
        new_institution = Institution.objects.get(pk=new_pk)
        return new_institution

    new_institution = Institution(
        name=old_institution.name,
        comment=old_institution.comment,
        modified_on=old_institution.modified,
        created_on=old_institution.created,
    )
    new_institution.save()

    for old_tag in old_institution.tags.all():
        new_tag = migrate_tag(old_tag)
        new_institution.tags.add(new_tag)

    fix_timestamps(new_institution, old_institution)

    PkMappings.institution[old_institution.pk] = new_institution.pk
    return new_institution


def migrate_persons():
    for old_person in models_v1.Person.objects.using(MIGRATION_DB).all():
        migrate_person(old_person)


def migrate_person(old_person):
    logger.debug("Migrating Person: %s", old_person.name)
    assert old_person.user is not None, f"{old_person} must have a relation to User"
    user = migrate_user(old_person.user)
    return user


def migrate_users():
    for old_user in get_user_model().objects.using(MIGRATION_DB).all():
        migrate_user(old_user)


def migrate_user(old_user):
    logger.debug("Migrating User: %s", old_user.username)
    if old_user.pk in PkMappings.user:
        new_pk = PkMappings.user[old_user.pk]
        logger.debug("Using cached User with pk == %a", new_pk)
        new_user = get_user_model().objects.get(pk=new_pk)
        return new_user

    old_pk = old_user.pk
    old_user.pk = None
    old_user.save(using=V2_DB)
    # Now we should get User instance from PostgreSQL with no problem
    new_user = get_user_model().objects.get(pk=old_user.pk)
    PkMappings.user[old_pk] = new_user.pk
    return new_user


def migrate_features():
    for old_dict in models_v1.Dictionary.objects.using(MIGRATION_DB).all():
        migrate_feature(old_dict)


def migrate_feature(old_dictionary):
    feature_name = old_dictionary.TYPE[old_dictionary.type]
    logger.debug("Migrating Feature: %s", feature_name)
    try:
        new_feature = Feature.objects.get(name=feature_name)
    except Feature.DoesNotExist:
        new_feature = Feature(name=feature_name)
        new_feature.save()
        fix_timestamps(new_feature, old_dictionary)
    except Feature.MultipleObjectsReturned:
        raise RuntimeError("Data duplication detected")

    feature_option_name = old_dictionary.name
    logger.debug("Migrating FeatureOption: %s -> %s", feature_name, feature_option_name)
    try:
        new_feature_option = FeatureOption.objects.get(
            name=feature_option_name,
            feature=new_feature,
        )
    except FeatureOption.DoesNotExist:
        new_feature_option = FeatureOption(
            name=feature_option_name, feature=new_feature
        )
        new_feature_option.save()
    except FeatureOption.MultipleObjectsReturned:
        raise RuntimeError("Data duplication detected")

    return new_feature_option


def migrate_cases():
    for old_case in models_v1.Case.objects.using(MIGRATION_DB).all():
        migrate_case(old_case)


def migrate_case(old_case):
    logger.debug("Migrating Case: %s (%s)", old_case.name, old_case.comment[:100])
    if old_case.pk in PkMappings.case:
        new_pk = PkMappings.case[old_case.pk]
        logger.debug("Using cached Case with pk == %a", new_pk)
        new_case = Case.objects.get(pk=new_pk)
        return new_case

    new_case = Case(
        name=old_case.name,
        comment=old_case.comment,
    )
    new_case.save()

    for old_tag in old_case.tags.all():
        new_tag = migrate_tag(old_tag)
        new_case.tags.add(new_tag)

    old_institution = old_case.audited_institution
    if old_institution:
        new_institution = migrate_institution(old_institution)
        new_case.audited_institutions.add(new_institution)

    for old_person in old_case.responsible_people.all():
        new_person = migrate_person(old_person)
        new_case.responsible_users.add(new_person)
        new_case.notified_users.add(new_person)

    feature_fields = [
        "whose_case",
        "what_scope",
        "inaction_scope",
        "decision_scope",
        "time_of_info_provide",
        "proceddings_interrupted",
        "status",
    ]
    for field in feature_fields:
        for old_dict in getattr(old_case, field).all():
            new_feature_option = migrate_feature(old_dict)
            new_case.featureoptions.add(new_feature_option)

    fix_timestamps(new_case, old_case)

    PkMappings.case[old_case.pk] = new_case.pk
    return new_case


def migrate_channels():
    for old_channel in models_v1.Channel.objects.using(MIGRATION_DB).all():
        migrate_channel(old_channel)


def migrate_channel(old_channel):
    logger.debug("Migrating Channel: %s", old_channel.name)
    try:
        new_channel = Channel.objects.get(name=old_channel.name)
    except Channel.DoesNotExist:
        new_channel = Channel(name=old_channel.name)
        new_channel.save()
        fix_timestamps(new_channel, old_channel)
    except Channel.MultipleObjectsReturned:
        raise RuntimeError("Data duplication detected")

    return new_channel


def migrate_letternames():
    for old_lettername in models_v1.LetterName.objects.using(MIGRATION_DB).all():
        migrate_lettername(old_lettername)


def migrate_lettername(old_lettername):
    logger.debug("Migrating LetterName: %s", old_lettername.content)
    try:
        new_document_type = DocumentType.objects.get(name=old_lettername.content)
    except DocumentType.DoesNotExist:
        new_document_type = DocumentType(name=old_lettername.content)
        new_document_type.save()
        # Note: DocumentType has no timestamps
    except DocumentType.MultipleObjectsReturned:
        raise RuntimeError("Data duplication detected")

    return new_document_type


def migrate_letters():
    for old_letter in models_v1.Letter.objects.using(MIGRATION_DB).all():
        migrate_letter(old_letter)


def migrate_letter(old_letter):
    logger.debug("Migrating Letter: %s", old_letter.name)
    direction_dict = {"R": "IN", "S": "OUT"}
    new_direction = Letter.Direction[direction_dict[old_letter.direction]]
    warsaw = timezone("Europe/Warsaw")
    new_date = warsaw.localize(
        datetime(
            year=old_letter.data.year,
            month=old_letter.data.month,
            day=old_letter.data.day,
        )
    )

    new_letter = Letter(
        direction=new_direction,
        date=new_date,
        comment=old_letter.comment,
        document_type=migrate_lettername(old_letter.name),
        # excerpt=???
        reference_number=old_letter.identifier,
    )
    if old_letter.institution:
        new_letter.institution = migrate_institution(old_letter.institution)
    if old_letter.case:
        new_letter.case = migrate_case(old_letter.case)
    if old_letter.channel:
        new_letter.channel = migrate_channel(old_letter.channel)

    new_letter.save()

    fix_timestamps(new_letter, old_letter)

    file = File(
        path=f"{uuid4()}/{old_letter.attachment.name}",
        name=old_letter.attachment.name,
        letter=new_letter,
    )
    file.save()

    return new_letter, file


def run(clean=False):
    if clean:
        logger.info("Cleaning models.")
        File.objects.all().delete()
        Letter.objects.all().delete()
        Institution.objects.all().delete()
        Case.objects.all().delete()
        Tag.objects.all().delete()
        Feature.objects.all().delete()
        FeatureOption.objects.all().delete()
        Channel.objects.all().delete()
        DocumentType.objects.all().delete()
        get_user_model().objects.all().delete()

    logger.info("Running v1 -> v2 data migration")
    with transaction.atomic(using=V2_DB):
        migrate_users()
        migrate_persons()
        migrate_letternames()
        migrate_channels()
        migrate_institutions()
        migrate_features()
        migrate_cases()
        migrate_letters()
    logger.info("Done.")
