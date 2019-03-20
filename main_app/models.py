from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# If A belongs to B, A holds fk (id of B) and if 
# upon deletion of B, A also needs to be deleted, than include cascade delete
# Create your models here.
 



class Location(models.Model):
    name = models.CharField(max_length=100)
    street = models.TextField(max_length=240)
    city = models.TextField(max_length=50)
    state = models.TextField(max_length=2)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Artist(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"    

class Appointment(models.Model):
    date = models.DateField('Date')
    time = models.TimeField('Time')
    completed = models.BooleanField()

class Tattoo(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=240)
    available = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}"
   
class JoinTable(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} {self.url}"