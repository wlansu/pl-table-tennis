# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('table_tennis', '0006_auto_20140612_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChampionShip',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of the championship')),
                ('year', models.PositiveIntegerField(null=True, blank=True, verbose_name='Year',
                                                     help_text='If this is the yearly competition fill in the year, '
                                                               'otherwise leave it blank.')),
            ],
            options={
                'ordering': ('year', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChampionShipRound',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('round_number', models.PositiveIntegerField(verbose_name='Round number')),
                ('championship', models.ForeignKey(to_field='id', to='table_tennis.ChampionShip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='competing_in_championships',
            field=models.ManyToManyField(to='table_tennis.ChampionShip'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='championshippairing',
            name='round_number',
            field=models.ForeignKey(to='table_tennis.ChampionShipRound', to_field='id', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='championshippairing',
            name='winner',
            field=models.ForeignKey(to='table_tennis.Player', to_field='id', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='championshippairing',
            name='loser',
            field=models.ForeignKey(to='table_tennis.Player', to_field='id', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='match',
            name='championship_match',
        ),
        migrations.RemoveField(
            model_name='player',
            name='competing_in_championship',
        ),
    ]
