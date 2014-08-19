# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('games_won', models.PositiveIntegerField(verbose_name='Games won by the winner of this match.')),
                ('games_lost', models.PositiveIntegerField(verbose_name='Games lost by the winner of this match.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('points', models.PositiveIntegerField(default=0, verbose_name='Points')),
                ('rank', models.PositiveIntegerField(verbose_name='Rank', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IndividualMatch',
            fields=[
                ('match_ptr', models.OneToOneField(serialize=False, to_field='id', primary_key=True, auto_created=True, to='table_tennis.Match')),
                ('won', models.ForeignKey(to_field='id', to='table_tennis.Player')),
                ('lost', models.ForeignKey(to_field='id', to='table_tennis.Player')),
            ],
            options={
            },
            bases=('table_tennis.match',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('player1', models.ForeignKey(to_field='id', to='table_tennis.Player')),
                ('player2', models.ForeignKey(to_field='id', to='table_tennis.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
