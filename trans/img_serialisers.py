from rest_framework import serializers
from models import PhotoUpload

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = PhotoUpload
        fields = ('id', 'date_created', 'image')
