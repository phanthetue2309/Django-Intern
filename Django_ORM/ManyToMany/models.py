from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=255)

class Machine(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField(
        Worker,
        related_name='Machine'
    )