# Generated by Django 3.1.1 on 2020-10-22 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyfinder', '0005_userprofile_student_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hide_school',
            field=models.BooleanField(default=False),
        ),
    ]
