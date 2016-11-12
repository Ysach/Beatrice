"""Beatrice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from trans import urls as media_urls
from rest_framework import routers
# from trans import img_urls
from trans import views
# from trans import img_views
from django.conf.urls.static import static
from django.conf import settings
from trans import img_views, media_views

router = routers.DefaultRouter()
# router.register(r'^media', media_views.MediaViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='dashboard'),
    url("^multi_file_transfer/$", views.multi_file_transfer, name="multi_file_transfer"),
    url(r'^media/', include(media_urls)),
    # url(r'^images/', include(img_urls)),
    # url("^detail/$", views.detail, name="detail"),

    url("^login/$", views.acc_login, name="login"),
    url("^logout/$", views.acc_logout, name="logout"),
    url("^file_trans/$", views.file_trans, name="file_trans"),
    url("^edit_media/$", views.edit_media, name="edit_media"),
    url(r'^', include(router.urls)),
    url(r'^img/$', img_views.photo_servers),
    url(r'^media/$', media_views.media_servers),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
