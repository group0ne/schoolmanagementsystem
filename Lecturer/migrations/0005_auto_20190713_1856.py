# Generated by Django 2.2.3 on 2019-07-13 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lecturer', '0004_auto_20190713_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='StudentName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
