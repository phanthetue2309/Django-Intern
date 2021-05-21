from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from People.models import Provider

# Create your models here.
class TypeProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Calculation_Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, related_name="products")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,null=True)
    calculationUnit = models.ForeignKey(Calculation_Unit, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    unit_cost = models.IntegerField(default=10000)
    selling_price = models.IntegerField(default=10000, null=True)
    origin = models.CharField(max_length=255)  # xuất xứ
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Product:list-product')

    class Meta:
        ordering = ['type_product__name']