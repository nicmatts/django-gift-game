# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='order',
            field=models.CharField(default=game.models.random_string, max_length=20),
        ),
    ]
