# Generated by Django 3.2 on 2021-07-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turntableApp', '0017_jie_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='pei_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
