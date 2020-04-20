# Generated by Django 2.2.4 on 2020-04-17 11:58

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foundationtask_group', to='otree.Session')),
            ],
            options={
                'db_table': 'foundationtask_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foundationtask_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'foundationtask_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('code', otree.db.models.StringField(max_length=10000, null=True)),
                ('groupp', otree.db.models.StringField(max_length=10000, null=True)),
                ('p1', otree.db.models.IntegerField(choices=[(0, 0), (20, 20), (40, 40), (60, 60), (80, 80), (100, 100), (120, 120), (140, 140), (160, 160), (180, 180), (200, 200), (220, 220), (240, 240), (260, 260), (280, 280), (300, 300), (320, 320), (340, 340), (360, 360), (380, 380), (400, 400), (420, 420), (440, 440), (460, 460), (480, 480), (500, 500)], null=True)),
                ('p2', otree.db.models.IntegerField(choices=[(0, 0), (20, 20), (40, 40), (60, 60), (80, 80), (100, 100), (120, 120), (140, 140), (160, 160), (180, 180), (200, 200), (220, 220), (240, 240), (260, 260), (280, 280), (300, 300), (320, 320), (340, 340), (360, 360), (380, 380), (400, 400), (420, 420), (440, 440), (460, 460), (480, 480), (500, 500)], null=True)),
                ('p3', otree.db.models.IntegerField(choices=[(0, 0), (20, 20), (40, 40), (60, 60), (80, 80), (100, 100), (120, 120), (140, 140), (160, 160), (180, 180), (200, 200), (220, 220), (240, 240), (260, 260), (280, 280), (300, 300), (320, 320), (340, 340), (360, 360), (380, 380), (400, 400), (420, 420), (440, 440), (460, 460), (480, 480), (500, 500)], null=True)),
                ('p4', otree.db.models.IntegerField(choices=[(0, 0), (20, 20), (40, 40), (60, 60), (80, 80), (100, 100), (120, 120), (140, 140), (160, 160), (180, 180), (200, 200), (220, 220), (240, 240), (260, 260), (280, 280), (300, 300), (320, 320), (340, 340), (360, 360), (380, 380), (400, 400), (420, 420), (440, 440), (460, 460), (480, 480), (500, 500)], null=True)),
                ('p5', otree.db.models.IntegerField(choices=[(0, 0), (20, 20), (40, 40), (60, 60), (80, 80), (100, 100), (120, 120), (140, 140), (160, 160), (180, 180), (200, 200), (220, 220), (240, 240), (260, 260), (280, 280), (300, 300), (320, 320), (340, 340), (360, 360), (380, 380), (400, 400), (420, 420), (440, 440), (460, 460), (480, 480), (500, 500)], null=True)),
                ('p6', otree.db.models.IntegerField(choices=[(0, 0), (20, 20), (40, 40), (60, 60), (80, 80), (100, 100), (120, 120), (140, 140), (160, 160), (180, 180), (200, 200), (220, 220), (240, 240), (260, 260), (280, 280), (300, 300), (320, 320), (340, 340), (360, 360), (380, 380), (400, 400), (420, 420), (440, 440), (460, 460), (480, 480), (500, 500)], null=True)),
                ('consensus', otree.db.models.FloatField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foundationtask.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foundationtask_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foundationtask_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundationtask.Subsession')),
            ],
            options={
                'db_table': 'foundationtask_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundationtask.Subsession'),
        ),
    ]
