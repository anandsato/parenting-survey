# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='max_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='min_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='multiplier',
            field=models.DecimalField(default=0.5, max_digits=5, decimal_places=2),
        ),
    ]
