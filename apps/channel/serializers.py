from rest_framework.serializers import ModelSerializer
from .models import Channel, Post


class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
