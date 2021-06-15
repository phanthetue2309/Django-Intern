from django.urls import path, include
from django.contrib import admin
from Album.views import *
from Instrument.views import *
from rest_framework import routers
from .views import *

admin.autodiscover()
router = routers.DefaultRouter()
router.register('album-test',AlbumViewSet,basename='album_test')
router.register('instrument-test',InstrumentViewSet,basename='instrument_test')

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    path('groups2/', GroupList2.as_view()),
    path('list/album/', AlbumList.as_view()),
    # path('create/album/', CreateAlbum.as_view()),
    # path('edit/album/<int:pk>', UpdateAlbum.as_view()),
    path('album-update/<int:pk>', HandleAlbum.as_view()),
    path('api/',include(router.urls))
    # ...
]
