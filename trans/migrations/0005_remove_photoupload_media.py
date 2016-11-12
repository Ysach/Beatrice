# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0004_mediaupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoupload',
            name='media',
        ),
    ]
