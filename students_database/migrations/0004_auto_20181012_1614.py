# Generated by Django 2.1.1 on 2018-10-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_database', '0003_auto_20181012_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]