from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from unicorn.api.views import *

router = DefaultRouter() 
router.register('unicorn-viewset', UnicornViewSet, basename='unicorn_vs')
router.register('unicorn-generic-viewset', UnicornGenericViewSet, basename='unicorn_gvs')
router.register('unicorn-model-viewset', UnicornModelViewSet, basename='unicorn_mvs')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('users.urls')),
    # API
    path('api/', include(router.urls)),
]

