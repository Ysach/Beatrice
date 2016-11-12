# _*_coding:utf-8_*_
import os, random
from Beatrice import settings


def json_date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d %T")


def handle_upload_file(request,file_obj):
    random_dir = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890', 10))
    # upload_dir = '%s/%s' %(settings.FileUploadDir, request.user.id)
    upload_dir = '%s/' % (settings.FileUploadDir,)
    upload_dir2 = '%s/%s' %(upload_dir,random_dir)
    if not os.path.isdir(upload_dir):
        os.mkdir(upload_dir)
    '''
    if not os.path.isdir(upload_dir2):
        os.mkdir(upload_dir2)
    '''
    with open('%s/%s' % (upload_dir, file_obj.name), 'wb') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    return "%s" % (file_obj.name,)
