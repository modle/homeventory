# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=50)),
                ('item_location', models.CharField(max_length=50)),
                ('item_quantity', models.IntegerField(default=1)),
                ('entered_date', models.DateTimeField()),
            ],
        ),
    ]
