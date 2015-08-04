# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_name', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i', models.CharField(max_length=300, verbose_name=b'title')),
                ('path', models.CharField(max_length=300)),
                ('visitors', models.IntegerField()),
                ('change', models.IntegerField()),
                ('domain_id', models.ForeignKey(to='concurrents_increase.Domain')),
            ],
        ),
    ]
