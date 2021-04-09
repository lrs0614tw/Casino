# Generated by Django 3.1.7 on 2021-04-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turntableApp', '0005_claire_done_spinwheel_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='hui_Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('prize', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
