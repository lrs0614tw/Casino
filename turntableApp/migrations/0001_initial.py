# Generated by Django 3.2 on 2021-08-08 16:39

import datetime
from django.db import migrations, models
import turntableApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ci_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='claire_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
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
                ('email', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='heysongUid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='hui_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='jie_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='pei_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prize_Rate',
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
            name='puduImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(default='uploads\\product-1.jpg', upload_to=turntableApp.models.get_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='puduMgms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('old', models.CharField(default='', max_length=50)),
                ('new', models.CharField(default='', max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='scratchDemo_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='slot_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('score', models.CharField(blank=True, max_length=255)),
                ('invite', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='snake_Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('picture', models.CharField(default='', max_length=100)),
                ('highscore', models.IntegerField()),
                ('prize', models.CharField(default='', max_length=500)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traveltobuys_Prize_Rate',
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
            name='Traveltobuys_User_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traveltobuys_Winner_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userdemo_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='wen_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Winner_Done',
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
