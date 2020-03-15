# Generated by Django 3.0.3 on 2020-03-10 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Date of the modification')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('name', models.CharField(help_text='Name of feature.', max_length=100, verbose_name='Name')),
                ('min_options', models.IntegerField(default=1, help_text='Minimum number of selected option (if any).', verbose_name='Min. options')),
                ('max_options', models.IntegerField(default=1, help_text='Maximum number of selected option.', verbose_name='Max. options')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='feature_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='feature_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='FeatureOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of option.', max_length=100, verbose_name='Name')),
                ('feature', models.ForeignKey(help_text='Related feature.', on_delete=django.db.models.deletion.CASCADE, to='features.Feature', verbose_name='Feature')),
            ],
        ),
    ]
