from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import *

# Create your views here.

# class Home(CreateView):
#     model = Event
#     fields = '__all__'

class Home(TemplateView):
    template_name = 'home1.html'
    def get_context_data(self, **kwargs):
        context= {'data': 'data'}
        return context
class About(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Artist(TemplateView):
    template_name = 'artists.html'

class Tattoo(TemplateView):
    template_name = 'tattoos.html'

class Appointment(TemplateView):
    template_name = 'appointments.html'