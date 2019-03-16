from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Artist(TemplateView):
    template_name = 'artists.html'