from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# If A belongs to B, A holds fk (id of B) and if 
# upon deletion of B, A also needs to be deleted, than include cascade delete
# Create your models here.
 



class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=240)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    

class Appointment(models.Model):
    date = models.DateField('Date')
    time = models.TimeField('Time')
    completed = models.BooleanField()

class Tattoo(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=240)
    available = models.BooleanField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=100)
   
class JoinTable(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


