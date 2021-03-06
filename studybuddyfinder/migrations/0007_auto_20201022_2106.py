# Generated by Django 3.1.1 on 2020-10-23 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyfinder', '0006_userprofile_hide_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hide_major',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hide_username',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hide_year',
            field=models.BooleanField(default=False),
        ),
    ]
