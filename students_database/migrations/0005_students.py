# Generated by Django 2.1.1 on 2018-10-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students_database', '0004_auto_20181012_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=50)),
                ('guard', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students_database.Guardian')),
            ],
        ),
    ]