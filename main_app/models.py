from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    adress = models.CharField(max_length=200)
    birthday = models.DateField('Date')
    