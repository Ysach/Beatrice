# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0003_photoupload_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('media', models.FileField(default=b'Media/None/No-media', upload_to=b'Media/')),
            ],
        ),
    ]
