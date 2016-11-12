# _*_coding: utf-8_*_
from rest_framework import viewsets
from img_serialisers import PhotoSerializer
from rest_framework import status
# from rest_framework import permissions
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from rest_framework.decorators import permission_classes
from rest_framework.response import Response
import models
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from rest_framework import generics
# import datetime
from django.contrib.sites.shortcuts import get_current_site
import urllib


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = models.PhotoUpload.objects.all()
    serializer_class = PhotoSerializer


@api_view(['POST'])
# @permission_classes((permissions.IsAuthenticated,))
def photo_servers(request):
    if request.method == 'GET':
        photo_info = models.PhotoUpload.objects.all()
        serializer = PhotoSerializer(photo_info, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)
        # 错误请求返回
        err_msg = {"msg": "上传的格式不对，请上传图片格式的文件", "status": -1}
        if serializer.is_valid():
            serializer.save()
            data = urllib.unquote(serializer.data['image'])
            # print serializer.data['image']
            full_url = ''.join(['http://', get_current_site(request).domain, data])
            image = {"image": full_url}
            return Response(image, status=status.HTTP_201_CREATED)
        return Response(err_msg, status=status.HTTP_200_OK)


