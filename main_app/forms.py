from django.forms import ModelForm
from .models import *

# class Profile(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name', 'username', 'password', 'email']


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['day','start_time','artist','location']
        widgets = {
                'day': forms.DateTimeInput(attrs={'id': 'datetime-input'}),
                'start_time': forms.DateTimeInput(attrs={'id': 'timepicker'}),
                'artist': forms.Select(attrs={'class':'input-field'})
            }
