# Generated by Django 2.2.4 on 2020-02-17 22:13

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cognitivenoise', '0002_auto_20200217_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='choice',
            field=otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], null=True),
        ),
    ]
