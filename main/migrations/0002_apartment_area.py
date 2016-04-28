# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='area',
            field=models.ForeignKey(blank=True, to='main.Area', null=True),
        ),
    ]
