from rest_framework import serializers
from models import MediaUpload

class MediaSerializer(serializers.ModelSerializer):
    media = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = MediaUpload
        fields = ('id', 'date_created', 'media')
