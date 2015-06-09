# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_item_item_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_color',
            field=models.CharField(default='bluelol', max_length=50),
        ),
    ]
