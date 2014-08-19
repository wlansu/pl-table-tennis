# encoding: utf8
from __future__ import unicode_literals

import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('table_tennis', '0005_auto_20140611_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='competing_in_championship',
            field=models.BooleanField(verbose_name='Is currently competing in a championship', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='date_played',
            field=models.DateField(verbose_name='Date this match was played.', default=datetime.date(2014, 6, 12)),
        ),
    ]
