from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework.views import APIView

class CustomerListAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class CustomerDetailAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Customer.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()