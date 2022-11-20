from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Pracownicy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

class Produkt(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))] )

class Zamowienia(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productid = models.ForeignKey(Produkt, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=True)


# Create your models here.
