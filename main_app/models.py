from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db import models
# from django.contrib.auth.models import User

# If A belongs to B, A holds fk (id of B) and if 
# upon deletion of B, A also needs to be deleted, than include cascade delete
# Create your models here.
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=240)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    social_media = ArrayField(ArrayField(
            models.CharField(max_length=10, blank=True),
            size=2,
        ),
        size=2,
    )

class Artist(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    

class Appointment(models.Model):
    date = models.DateField('Date')
    time = models.TimeField('Time')
    completed = models.BooleanField()
    
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Tattoo(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=240)
    available = models.BooleanField()
    
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

class MyUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    birthday = models.DateField('Date')
    
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    