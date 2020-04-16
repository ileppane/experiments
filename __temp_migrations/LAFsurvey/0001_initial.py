# Generated by Django 2.2.4 on 2020-03-31 21:19

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lafsurvey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'LAFsurvey_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lafsurvey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'LAFsurvey_subsession',
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
                ('name', otree.db.models.StringField(max_length=10000, null=True)),
                ('email', otree.db.models.StringField(max_length=10000, null=True)),
                ('student_number', otree.db.models.StringField(max_length=10000, null=True)),
                ('allportth', otree.db.models.PositiveIntegerField(null=True)),
                ('allportec', otree.db.models.PositiveIntegerField(null=True)),
                ('allportpo', otree.db.models.PositiveIntegerField(null=True)),
                ('allportae', otree.db.models.PositiveIntegerField(null=True)),
                ('allportso', otree.db.models.PositiveIntegerField(null=True)),
                ('allportre', otree.db.models.PositiveIntegerField(null=True)),
                ('nfcscore', otree.db.models.PositiveIntegerField(null=True)),
                ('fiscore', otree.db.models.PositiveIntegerField(null=True)),
                ('q1a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q1b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q2a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q2b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q3a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q3b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q4a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q4b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q5a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q5b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q6a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q6b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q7a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q7b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q8a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q8b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q9a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q9b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q10a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q10b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q11a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q11b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q12a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q12b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q13a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q13b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q14a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q14b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q15a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q15b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q16a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q16b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q17a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q17b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q18a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q18b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q19a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q19b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q20a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q20b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q21a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q21b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q22a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q22b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q23a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q23b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q24a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q24b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q25a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q25b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q26a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q26b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q27a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q27b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q28a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q28b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q29a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q29b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q30a', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('q30b', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True)),
                ('qq1a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq1b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq1c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq1d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq2a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq2b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq2c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq2d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq3a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq3b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq3c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq3d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq4a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq4b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq4c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq4d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq5a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq5b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq5c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq5d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq6a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq6b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq6c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq6d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq7a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq7b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq7c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq7d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq8a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq8b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq8c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq8d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq9a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq9b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq9c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq9d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq10a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq10b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq10c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq10d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq11a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq11b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq11c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq11d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq12a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq12b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq12c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq12d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq13a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq13b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq13c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq13d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq14a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq14b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq14c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq14d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq15a', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq15b', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq15c', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('qq15d', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('q1', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q2', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q3', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q4', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q5', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q6', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q7', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q8', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q9', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q10', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q11', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q12', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q13', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q14', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q15', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q16', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q17', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q18', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q19', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q20', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q21', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q22', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q23', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q24', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q25', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q26', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q27', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q28', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q29', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q30', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q31', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAFsurvey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lafsurvey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lafsurvey_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LAFsurvey.Subsession')),
            ],
            options={
                'db_table': 'LAFsurvey_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LAFsurvey.Subsession'),
        ),
    ]
