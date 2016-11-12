
from django.conf.urls import include, url
import views

urlpatterns = [
    # url("^$", views.hosts_index, name="hosts"),
    url("^submit_task/$", views.submit_task, name="submit_task"),
    url("^file_upload/$", views.file_upload, name="file_upload"),
    url("^media_del/$", views.delete_media, name="media_del"),

]
