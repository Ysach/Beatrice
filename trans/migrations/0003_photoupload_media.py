# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0002_photoupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoupload',
            name='media',
            field=models.FileField(default=b'Media/None/No-media', upload_to=b'Media/'),
        ),
    ]
