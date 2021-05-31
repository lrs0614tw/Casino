# Generated by Django 3.2 on 2021-05-29 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turntableApp', '0013_heysonguid'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeysongScratch_Prize_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('rate', models.CharField(blank=True, max_length=255)),
                ('left', models.CharField(blank=True, max_length=255)),
                ('today', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='HeysongScratch_User_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeysongScratch_Winner_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]