from django.conf.urls import url, include
from rest_framework import routers
import img_views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

router.register(r'^img', img_views.PhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^img/$', img_views.photo_servers),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
