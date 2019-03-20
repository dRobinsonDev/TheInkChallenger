from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.urls import reverse
from django import forms
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


class Event(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


    
 
    class Meta:
        verbose_name = u'Schedules'
        verbose_name_plural = u'Schedules'
 
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
 
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending time must be after starting time')
 
        events = Event.objects.filter(day=self.day, artist=self.artist)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))