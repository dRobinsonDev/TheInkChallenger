from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    adress = models.CharField(max_length=200)
    birthday = models.DateField('Date')
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    adress = models.CharField(max_length=200)

