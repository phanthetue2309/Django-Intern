from django.db import models

#DataFlair #DjangoTutorials
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(  # this is one to many 
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )