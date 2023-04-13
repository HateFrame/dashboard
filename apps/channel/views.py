from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Channel, Post
from .serializers import ChannelSerializer, PostSerializer


class ChannelViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    queryset = Channel.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ChannelSerializer


class PostViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = PostSerializer
