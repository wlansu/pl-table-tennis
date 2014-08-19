# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('table_tennis', '0002_teammatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='date_played',
            field=models.DateField(default=datetime.date(2014, 6, 5), verbose_name='Date this match was played.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='games_lost',
            field=models.PositiveIntegerField(verbose_name='Games lost the winner.'),
        ),
        migrations.AlterField(
            model_name='match',
            name='games_won',
            field=models.PositiveIntegerField(verbose_name='Games won by winner.'),
        ),
    ]
