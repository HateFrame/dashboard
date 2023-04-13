from django.contrib import admin
from django.urls import path, include


api_patterns = [
    path('', include('apps.channel.urls')),
    path('', include('apps.dashboard.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns))
]
