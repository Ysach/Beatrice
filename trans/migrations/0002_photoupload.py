# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default=b'Images/None/No-img.jpg', upload_to=b'Images/')),
            ],
        ),
    ]
