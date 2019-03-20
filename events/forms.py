from django.forms import ModelForm
from .models import *

class FeedingForm(ModelForm):
  class Meta:
    model = Event
    fields = ['day', 'start_time', 'notes']