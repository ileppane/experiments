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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dsraq_group', to='otree.Session')),
            ],
            options={
                'db_table': 'dsraq_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dsraq_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'dsraq_subsession',
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
                ('aq1', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq2', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq3', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq4', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq5', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq6', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq7', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq8', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq9', otree.db.models.PositiveIntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], null=True)),
                ('aq10', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq11', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq12', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq13', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq14', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq15', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq16', otree.db.models.PositiveIntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], null=True)),
                ('aq17', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq18', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq19', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq20', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq21', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq22', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq23', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq24', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq25', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq26', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq27', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq28', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('aq29', otree.db.models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('dsr1', otree.db.models.PositiveIntegerField(choices=[[1, 'F'], [0, 'T']], null=True)),
                ('dsr2', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr3', otree.db.models.PositiveIntegerField(choices=[[1, 'F'], [0, 'T']], null=True)),
                ('dsr4', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr5', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr6', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr7', otree.db.models.PositiveIntegerField(choices=[[1, 'F'], [0, 'T']], null=True)),
                ('dsr8', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr9', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr10', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr11', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr12', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr13', otree.db.models.PositiveIntegerField(choices=[[0, 'F'], [1, 'T']], null=True)),
                ('dsr14', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr15', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr16', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr17', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr18', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr19', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr20', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr21', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr22', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr23', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr24', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('dsr25', otree.db.models.FloatField(choices=[[0, '1'], [0.5, '2'], [1, '3']], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dsraq.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dsraq_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dsraq_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsraq.Subsession')),
            ],
            options={
                'db_table': 'dsraq_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsraq.Subsession'),
        ),
    ]
