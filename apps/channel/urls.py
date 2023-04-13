from rest_framework import routers

from .views import ChannelViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('channels', ChannelViewSet, basename='channels')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = router.urls
