# Generated by Django 2.2.3 on 2019-07-13 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lecturer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='LecturerName',
            new_name='StudentName',
        ),
    ]
