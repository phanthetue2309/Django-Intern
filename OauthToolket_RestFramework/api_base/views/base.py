from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    required_scopes = []
