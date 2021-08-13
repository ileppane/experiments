# Generated by Django 2.2.12 on 2021-08-06 14:21

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ECI_survey', '0008_remove_player_wtp_iphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='RM_reliable',
            field=otree.db.models.IntegerField(choices=[[1, '1 Very Unlikely'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, '7 Very Likely']], null=True),
        ),
    ]
