# Generated by Django 3.2 on 2021-04-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turntableApp', '0008_wen_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='snake_Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('picture', models.CharField(default='', max_length=100)),
                ('highscore', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(default='', max_length=500)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]