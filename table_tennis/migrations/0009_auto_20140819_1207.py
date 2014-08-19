# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('table_tennis', '0008_auto_20140613_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': (b'date_played',)},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': (b'rank', b'name')},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': (b'name',)},
        ),
        migrations.AlterField(
            model_name='match',
            name='date_played',
            field=models.DateField(default=datetime.date(2014, 8, 19), verbose_name='Date this match was played.'),
        ),
    ]
