# Generated by Django 2.2.12 on 2021-08-07 07:19

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ECI_survey', '0011_auto_20210807_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='RM_likelytobuy',
            field=otree.db.models.IntegerField(choices=[[1, 'Very Unlikely'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, 'Very Likely']], null=True),
        ),
    ]
