# Generated by Django 2.2.4 on 2020-03-05 09:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('eoq', '0013_player_freeform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='freeform',
            field=otree.db.models.LongStringField(null=True, verbose_name=''),
        ),
    ]
