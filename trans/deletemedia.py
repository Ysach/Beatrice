# _*_coding:utf-8_*_

from django.db import transaction
import models
from Beatrice import settings
from trans import md5sum
import os
import json
import subprocess
import shutil


class Delete(object):
    def __init__(self, request):
        self.request = request
        self.media_action = self.request.POST.get("media_action")

    def handle(self):
        if self.media_action:
            if hasattr(self, self.media_action):
                func = getattr(self, self.media_action)
                return func()
            else:
                raise TypeError

    # @transaction.atomic
    def media_action_del(self):
        print '=========going to del media=========='
        print '=========media action del=========', self.request.POST.get("media_name")

        media_temp = self.request.POST.get("media_name")
        media_wait_for_del = media_temp.split('/')[-1]
        media_while_del = settings.FileUploadDir + '/' + media_wait_for_del
        if os.path.exists(media_while_del):
            os.remove(media_while_del)

            db_update = models.FileUpload.objects.filter(
                new_name=media_wait_for_del,
            )
            db_update.delete()
        else:
            db_update = models.FileUpload.objects.filter(
                new_name=media_wait_for_del,
            )
            db_update.delete()






