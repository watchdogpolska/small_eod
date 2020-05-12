# Generated by Django 3.0.3 on 2020-02-21 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutions', '0006_auto_20200220_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='institution_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of creation'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='institution_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Date of the modification'),
        ),
    ]
