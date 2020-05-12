# Generated by Django 3.0.3 on 2020-03-10 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
        ('cases', '0008_auto_20200308_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='featureoptions',
            field=models.ManyToManyField(blank=True, help_text='Features options for this case.', to='features.FeatureOption', verbose_name='Feature option'),
        ),
    ]
