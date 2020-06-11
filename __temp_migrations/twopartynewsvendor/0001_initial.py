# Generated by Django 2.2.4 on 2020-06-10 02:48

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twopartynewsvendor_group', to='otree.Session')),
            ],
            options={
                'db_table': 'twopartynewsvendor_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='twopartynewsvendor_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'twopartynewsvendor_subsession',
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
                ('starttime', otree.db.models.FloatField(null=True)),
                ('endtime', otree.db.models.FloatField(null=True)),
                ('orderquantity', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True)),
                ('trueorderquantity', otree.db.models.PositiveIntegerField(null=True)),
                ('demand', otree.db.models.PositiveIntegerField(null=True)),
                ('custpay', otree.db.models.PositiveIntegerField(null=True)),
                ('check1low', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '936'], [2, '364'], [3, '858']], null=True)),
                ('check2low', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '0'], [2, '1/7'], [3, '5/7']], null=True)),
                ('check3low', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '5/7'], [2, '1/7'], [3, '2/7']], null=True)),
                ('check1high', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '560'], [2, '522'], [3, '662']], null=True)),
                ('check2high', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '0'], [2, '1/7'], [3, '5/7']], null=True)),
                ('check3high', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '5/7'], [2, '1/7'], [3, '2/7']], null=True)),
                ('check4', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, 'Not all customers can be satisfied'], [2, 'Nothing'], [3, 'Not all items can be sold']], null=True)),
                ('check5', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '£0.11'], [2, '£11.30'], [3, '£1.13']], null=True)),
                ('pecu', otree.db.models.PositiveIntegerField(choices=[[1, '1 = Not at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9 = As much as possible']], null=True)),
                ('nonpecu', otree.db.models.PositiveIntegerField(choices=[[1, '1 = Not at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9 = As much as possible']], null=True)),
                ('conflict', otree.db.models.PositiveIntegerField(choices=[[1, '1 = Least conflicted'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9 = Most conflicted']], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='twopartynewsvendor.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twopartynewsvendor_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twopartynewsvendor_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twopartynewsvendor.Subsession')),
            ],
            options={
                'db_table': 'twopartynewsvendor_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twopartynewsvendor.Subsession'),
        ),
    ]
