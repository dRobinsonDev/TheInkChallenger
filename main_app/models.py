# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse
from django import forms
# If A belongs to B, A holds fk (id of B) and if 
# upon deleti
# on of B, A also needs to be deleted, than include cascade delete
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
    url = models.CharField(max_length=100, default='')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150, default=None)
    phone_number = models.CharField(max_length=100, default=None)
    tattoo = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.user}"
   

class Photo(models.Model):
    url = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} {self.url}"

c = Artist.objects.all()
choices = []
for choice in c:
    choices.append((choice.id, choice.name))

s = Location.objects.all()
shops = []
for shop in s:
    shops.append((shop.id, shop.name))

class Event(models.Model):
    day = models.DateField(u'Day of the event')
    start_time = models.TimeField(u'Starting time')
    end_time = models.TimeField(u'Final time')
    notes = models.TextField(u'Textual Notes', blank=True, null=True)
    artist = models.IntegerField(choices=choices, default=choices[0])
    location = models.IntegerField(choices=shops, default=shops[0])
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
 
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap
 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
        # time.strftime(add hour)
 
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending time must be after starting time')
 
        events = Event.objects.filter(day=self.day, artist=self.artist)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There artist already has an appointment on : ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))

class JoinTable(models.Model):
    # appointment = models.ForeignKey(Event, on_delete=models.CASCADE)
    # tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    appointment = models.Integer()
    tattoo = models.Integer()
    artist = models.Integer()
    profile = models.Integer()
    location = models.Integer()
