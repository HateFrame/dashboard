from rest_framework import routers

from .views import LogViewSet

router = routers.DefaultRouter()
router.register('logs', LogViewSet, basename='logs')

urlpatterns = router.urls
