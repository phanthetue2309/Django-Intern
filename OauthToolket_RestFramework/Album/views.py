from django.shortcuts import render
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Album
from .serializers import AlbumSerializer

# Create your views here.
class AlbumList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['albums']
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class CreateAlbum(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['albums']
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class UpdateAlbum(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['albums']
    # TokenHasReadWriteScope and required_scopes will be render to scope='read write albums'
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'pk'

# Test Using API VIew run success
class HandleAlbum(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['albums']
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request):
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                return Response(str(e))

    def get_object(self, pk):
        try:
            album = Album.objects.get(id=pk)
            return album
        except Album.DoesNotExist:
            return Response("No contains data")

    def put(self, request, pk):
        serializer = AlbumSerializer(instance=self.get_object(pk), data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                return Response(str(e))

    def delete(self, request, pk):
        try :
            album = Album.objects.filter(id=pk)
            if not album.exists():
                raise Exception('Can not delete album not contains')
            return album.delete()
        except Exception as e:
            return Response(str(e))


# Test Using ViewSet
class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['albums']
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer






