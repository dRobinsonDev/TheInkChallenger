from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    birthday = models.DateField('Date')
    
    artists = models.OneToManyField(Artist)
    tattoos = models.OneToOneField(Tattoo)
    appointments = models.OneToOneField(Appointment)
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)

    location = models.ManyToManyField(Location)
    appointment = models.ManyToManyField(Appointment)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

class Appointment(models.Model):
    date = models.DateField('Date')
    time = models.TimeField('Time')
    completed = models.BooleanField()

    tattoos = models.OneToOneField(Tattoo)

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
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

class Tattoo(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=240)

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)




