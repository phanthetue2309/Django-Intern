from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer

# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupList2(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['users']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer