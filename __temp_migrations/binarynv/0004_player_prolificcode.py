# Generated by Django 2.2.12 on 2021-10-03 18:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('binarynv', '0003_auto_20210930_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='prolificcode',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
