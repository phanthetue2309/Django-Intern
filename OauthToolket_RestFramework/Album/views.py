from django.shortcuts import render
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, TokenMatchesOASRequirements
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Album
from .serializers import AlbumSerializer


# Test Using ViewSet
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def list(self, request, *args, **kwargs):
        required_scopes = ["albums:read"]
        return super(AlbumViewSet, self).list(request)




