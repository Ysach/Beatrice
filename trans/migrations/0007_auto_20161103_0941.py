# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0006_mediaupload_media_md5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaupload',
            name='media_md5',
            field=models.CharField(max_length=256),
        ),
    ]
