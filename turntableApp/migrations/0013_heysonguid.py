# Generated by Django 3.2 on 2021-05-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turntableApp', '0012_rename_spinwheel_done_scratchdemo_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='heysongUid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
