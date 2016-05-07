# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_apartment_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='gov',
            field=models.ForeignKey(blank=True, to='main.Gov', null=True),
        ),
    ]
