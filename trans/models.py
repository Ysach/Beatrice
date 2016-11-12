# _*_coding:utf-8_*_

from django.db import models

# Create your models here.
from customauth import UserProfile


class FileUpload(models.Model):
    original_name = models.CharField(max_length=64)
    new_name = models.CharField(max_length=64, unique=True)
    expert_name = models.CharField(max_length=64)
    upload_user = models.CharField(max_length=128)
    upload_time = models.DateTimeField(auto_now_add=True)
    media_num = models.CharField(max_length=32)
    media_expert = models.CharField(max_length=32)


class PhotoUpload(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')


class MediaUpload(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='Media/', default='Media/None/No-media')
    media_md5 = models.CharField(max_length=256)
