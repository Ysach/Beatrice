# _*_coding:utf-8_*_
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import models, task, json, utils, deletemedia

from django.core.exceptions import ObjectDoesNotExist
import django.utils.timezone
# Create your views here.


@login_required
def index(request):
    file_all = models.FileUpload.objects.all()
    return render(request, 'index.html', {'file_all': file_all})


@login_required
def acc_logout(request):
    logout(request)

    return HttpResponseRedirect("/")


def acc_login(request):
    login_err = ''
    if request.method == 'POST':
        print '-------request post----', request.POST
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
           #  request.session.set_expiry(60*30)
            # 设置session超时时间
            return HttpResponseRedirect('/')

        else:
            login_err = "用户名或者密码错误!"
    return render(request, 'login.html', {'login_err': login_err})


@login_required
def multi_file_transfer(request):
    return render(request, "multi_file_transfer.html")


@login_required
def delete_media(request):
    # print '=========delete media =======================>', request.POST
    # print '=========delete media action =======================>', request.POST.get("media_action")
    media_obj = deletemedia.Delete(request)
    media_res = media_obj.handle()
    return HttpResponse(json.dumps(media_res))


@login_required
def submit_task(request):
    tas_obj = task.Task(request)
    res = tas_obj.handle()

    return HttpResponse(json.dumps(res))


@csrf_exempt
@login_required
def file_upload(request):
    filename = request.FILES['filename']
    # print '----------------file upload------------------->', request.POST
    file_path = utils.handle_upload_file(request, filename)

    return HttpResponse(json.dumps({'uploaded_file_path': file_path}))


@login_required
def detail(request):

    return render(request, 'detail.html')


@login_required
def file_trans(request):
    return render(request, 'file_upload.html')


@login_required
def edit_media(request):

    edit_err = ''
    if request.method == 'POST':

        print '=================media edit========>', request.POST
        media_name = request.POST.get('media_name')
        media_original = request.POST.get('media_original')
        media_expert = request.POST.get('media_expert')
        expert_name = request.POST.get('expert_username')

        # print '=================>', media_name
        # print '=================>', media_original

        db_data = models.FileUpload.objects.get(original_name=media_original, media_num=media_name)
        # print '================db===========', db_data

        if db_data:
            db_data.media_expert = media_expert
            db_data.expert_name = expert_name
            db_data.save()

        else:
            edit_err = "错误，请重新提交或者联系管理员"

    return render(request, 'edit_media.html', {'edit_err': edit_err})
