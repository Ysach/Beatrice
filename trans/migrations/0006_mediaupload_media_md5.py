# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0005_remove_photoupload_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaupload',
            name='media_md5',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
