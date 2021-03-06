from django.db import models
from django.utils.translation import gettext as _ # using in datetime
# Create your models here.


class AbstractPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45, null=True)
    phone_number = models.CharField(max_length=45, null=True)
    discription = models.TextField(null=True)

    def __str__(self):  # show the name of customer when print
        return self.name

    class Meta:
        abstract = True


class Customer(AbstractPerson):
    pass