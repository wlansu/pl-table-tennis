# encoding: utf8
from __future__ import unicode_literals

import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('table_tennis', '0003_auto_20140605_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChampionshipIndividualMatch',
            fields=[
                ('match_ptr',
                 models.OneToOneField(to='table_tennis.Match', primary_key=True, auto_created=True, serialize=False,
                                      to_field='id')),
                ('player1', models.ForeignKey(to='table_tennis.Player', to_field='id')),
                ('player2', models.ForeignKey(to='table_tennis.Player', to_field='id')),
                ('won', models.ForeignKey(to='table_tennis.Player', to_field='id')),
                ('lost', models.ForeignKey(to='table_tennis.Player', to_field='id')),
            ],
            options={
            },
            bases=('table_tennis.match',),
        ),
        migrations.AddField(
            model_name='match',
            name='championship_match',
            field=models.BooleanField(default=False, verbose_name='Championship match'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='date_played',
            field=models.DateField(default=datetime.date(2014, 6, 11), verbose_name='Date this match was played.'),
        ),
    ]
