# Generated by Django 3.2 on 2021-04-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turntableApp', '0010_alter_snake_player_highscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake_player',
            name='highscore',
            field=models.IntegerField(),
        ),
    ]
