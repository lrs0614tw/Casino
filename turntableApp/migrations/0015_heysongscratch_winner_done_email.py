# Generated by Django 3.2 on 2021-05-31 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turntableApp', '0014_heysongscratch_prize_rate_heysongscratch_user_done_heysongscratch_winner_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='heysongscratch_winner_done',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]