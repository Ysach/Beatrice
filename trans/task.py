# _*_coding:utf-8_*_

# from django.db import transaction
import models
from Beatrice import settings
from trans import md5sum
# import os
# import json
# import subprocess
import shutil


class Task(object):
    def __init__(self, request):
        self.request = request
        self.task_type = self.request.POST.get("task_type")

    def handle(self):
        if self.task_type:
            if hasattr(self, self.task_type):
                func = getattr(self, self.task_type)
                return func()
            else:
                raise TypeError

    # @transaction.atomic
    def multi_file_transfer(self):
        upload_files = self.request.POST.getlist("upload_files[]")
        index_username = self.request.POST.get("index_username")
        media_num = self.request.POST.get("media_num")

        # print '=======username======', index_username # 打印获取到的用户名
        # print '=========upload_files dic=======', data_dic # 打印字典值
        print '=========upload_files=======', upload_files # 打印上传的文件名
        for files in upload_files:
            # print '========files name=====', files, '==========', md5sum.md5(settings.FileUploadDir + '/' + files)
            old_file = settings.FileUploadDir + '/' + files
            new_file = settings.FileUploadDir + '/' + md5sum.md5(settings.FileUploadDir + '/' + files) + '.mp3'
            new_name = md5sum.md5(settings.FileUploadDir + '/' + files) + '.mp3'
            shutil.move(old_file, new_file)
            files = files.split('.mp3')[0]
            # shutil.move(old_file, '/var/www/html/' + new_name)
            # shutil.copy(new_file, '/var/www/html')
            # print '===new file===', new_file
            # print '-----md5-----', md5
            # print '=======files md5========', hashlib.md5(open(files, 'rb').read()).hexdigest()
            task_obj = models.FileUpload(
                original_name=files,
                # user_id=self.request.user.id,
                new_name=new_name,
                upload_user=index_username,
                media_num=media_num,
            )
            task_obj.save()
            # return {'upload_res': 'success'}



