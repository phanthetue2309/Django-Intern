from django.urls import path, include
from django.contrib import admin
from Album.views import *
from Instrument.views import *
from rest_framework import routers


admin.autodiscover()
router = routers.DefaultRouter()
router.register('album-test', AlbumViewSet, basename='album_test')
router.register('instrument-test', InstrumentViewSet, basename='instrument_test')

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include(router.urls)),
    path('authentication/', include('accounts.urls')),
    # ...
]
