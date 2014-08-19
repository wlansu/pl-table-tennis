# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table_tennis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMatch',
            fields=[
                ('match_ptr', models.OneToOneField(serialize=False, to_field='id', primary_key=True, auto_created=True, to='table_tennis.Match')),
                ('won', models.ManyToManyField(to='table_tennis.Team')),
                ('lost', models.ManyToManyField(to='table_tennis.Team')),
            ],
            options={
            },
            bases=('table_tennis.match',),
        ),
    ]
