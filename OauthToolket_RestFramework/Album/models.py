from django.db import models
from django.contrib.auth.models import User
from rest_framework import generics, permissions, serializers


class Album(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
