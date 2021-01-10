from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Post

class autocompleteSerializer(ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url']
    
    def get_url(self, obj):
        return obj.get_absolute_url()