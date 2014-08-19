# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('table_tennis', '0007_auto_20140612_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='championship',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Currently active.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='date_played',
            field=models.DateField(default=datetime.date(2014, 6, 13), verbose_name='Date this match was played.'),
        ),
    ]
