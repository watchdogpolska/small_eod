from django.db import migrations, models
from django.db.models import F
import django.db.models.deletion

def create_reference_numbers(apps, schema_editor):
    Letter = apps.get_model("letters", "Letter")
    ReferenceNumber = apps.get_model("letters", "ReferenceNumber")
    db_alias = schema_editor.connection.alias

    # Gather existing reference numbers.
    reference_numbers_names = Letter.objects.using(db_alias).values_list("reference_number", flat=True).distinct().order_by("reference_number")

    # Create a new model for each known reference number.
    reference_number_objs = ReferenceNumber.objects.using(db_alias).bulk_create([ReferenceNumber(name=reference_number) for reference_number in reference_numbers_names])
    reference_numbers_name_to_obj = { rn.name: rn for rn in reference_number_objs }

    # Reference new models in each Letter.
    letters = Letter.objects.using(db_alias).only("reference_number", "reference_number_temp").all()
    for l in letters:
        # We've iterated over all letters. Lookup should never fail.
        l.reference_number_temp = reference_numbers_name_to_obj[l.reference_number]
    Letter.objects.using(db_alias).bulk_update(letters, ['reference_number_temp'])

def reverse_create_reference_numbers(apps, schema_editor):
    Letter = apps.get_model("letters", "Letter")
    db_alias = schema_editor.connection.alias

    # Copy the related object's name into Letter's own field.
    letters = Letter.objects.using(db_alias).only("reference_number", "reference_number_temp").select_related("reference_number_temp").all()
    for l in letters:
        l.reference_number = l.reference_number_temp.name
    Letter.objects.using(db_alias).bulk_update(letters, ['reference_number'])


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0015_alters_for_v1_data_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Reference number of letter.', max_length=256, unique=True, verbose_name='Reference number')),
            ],
        ),
        # Add a temporary field to save new data to.
        # It will be renamed in a separate step.
        migrations.AddField(
            model_name='letter',
            name='reference_number_temp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='letters.referencenumber', verbose_name='Reference number'),
        ),
        # Copy values to a new field.
        migrations.RunPython(create_reference_numbers, reverse_create_reference_numbers),
        # Clean up old data.
        migrations.RemoveField(model_name='letter', name='reference_number'),
        migrations.RenameField(
            model_name='letter',
            old_name='reference_number_temp',
            new_name='reference_number',
        ),
    ]
