# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concurrents_increase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='change',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='visitors',
            field=models.IntegerField(default=0),
        ),
    ]
