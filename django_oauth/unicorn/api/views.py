from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from unicorn.models import Unicorn
from .serializer import UnicornSerializer


class UnicornViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Unicorn.objects.all()
        serializer = UnicornSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Unicorn.objects.all()
        unicorn = get_object_or_404(queryset, pk=pk)
        serializer = UnicornSerializer(unicorn)
        return Response(serializer.data)


class UnicornGenericViewSet(viewsets.GenericViewSet):

    def get_queryset(self):
        queryset = Unicorn.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UnicornSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        obj = self.get_object()
        serializer = UnicornSerializer(obj)
        return Response(serializer.data)


class UnicornModelViewSet(viewsets.ModelViewSet):
    queryset = Unicorn.objects.all()
    serializer_class = UnicornSerializer
