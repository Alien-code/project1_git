# Generated by Django 2.1.1 on 2018-10-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoollInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('district', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('stablished_date', models.DateField()),
            ],
        ),
    ]
