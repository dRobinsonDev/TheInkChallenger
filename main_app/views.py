from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import User, Artist, Location, Tattoo, Appointment, Profile, Photo


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context= {'data': 'data'}
        return context

class About(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Artist(ListView):
    template_name = 'artists.html'
    model = Artist
    context_object_name = 'artists'
    


class Tattoo(TemplateView):
    template_name = 'tattoos.html'

class Appointment(TemplateView):
    template_name = 'appointments.html'

def signup(request):
  error_message = ''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}

  class Meta:
    model = User 
  return render(request, 'registration/signup.html', context)
