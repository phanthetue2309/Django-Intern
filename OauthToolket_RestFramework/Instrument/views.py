from django.shortcuts import render
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Instrument
from .serializers import InstrumentSerializer


# Test Using ViewSet
class InstrumentViewSet(viewsets.ModelViewSet):

    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [TokenMatchesOASRequirements]
    # Phân scope cho từng cụm
    required_alternate_scopes = {
        "GET": [["get_public"]],
        "POST": [["create"]],
        "PUT":  [["update"]],
        "DELETE": [["delete"]],
    }

