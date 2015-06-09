# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20150603_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_size',
            field=models.IntegerField(default=1),
        ),
    ]
