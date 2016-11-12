# _*_coding: utf-8_*_
from rest_framework import viewsets
from media_serialisers import MediaSerializer
from rest_framework import status
# from rest_framework import permissions
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from rest_framework.decorators import permission_classes
from rest_framework.response import Response
import models
from django.contrib.sites.shortcuts import get_current_site
import urllib


class MediaViewSet(viewsets.ModelViewSet):
    queryset = models.MediaUpload.objects.all()
    serializer_class = MediaSerializer


@api_view(['GET', 'POST'])
# @permission_classes((permissions.IsAuthenticated,))
def media_servers(request):
    if request.method == 'GET':
        media_info = models.MediaUpload.objects.all()
        serializer = MediaSerializer(media_info, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MediaSerializer(data=request.data)
        # 错误请求返回
        err_msg = {"msg": "上传的格式不对，请上传图片格式的文件", "status": -1}
        if serializer.is_valid():
            serializer.save()
            # print serializer.data['media']
            data = urllib.unquote(serializer.data['media'])
            full_url = ''.join(['http://', get_current_site(request).domain, data])
            media = {"media": full_url}

            return Response(media, status=status.HTTP_201_CREATED)
        return Response(err_msg, status=status.HTTP_200_OK)


