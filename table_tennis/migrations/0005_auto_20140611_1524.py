# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('table_tennis', '0004_auto_20140611_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChampionshipPairing',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('player1', models.ForeignKey(to='table_tennis.Player', to_field='id')),
                ('player2', models.ForeignKey(to='table_tennis.Player', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='ChampionshipIndividualMatch',
        ),
    ]
