from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
import random
from .models import User, Artist, Location, Tattoo as TattooModel, Appointment, Profile, Photo
from .forms import *
from .utils import *



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

class ArtistList(ListView):
    template_name = 'artists.html'
    model = Artist
    context_object_name = 'artists'
    
class ShopList(ListView):
    template_name = 'shops.html'
    model = Location
    context_object_name = 'shops'

class TattooList(ListView):
    template_name = 'tattoos.html'
    model = Tattoo
    context_object_name = 'tattoos'

class Appointment(TemplateView):
    template_name = 'appointments.html'

def Create_Event(request):
    error_message = ''
    if 'randomTat' in request.session:
        error_message = request.session['randomTat']
    
    if request.method == "POST":
      event_form = EventForm(request.POST)
      if event_form.is_valid():
        data = event_form.cleaned_data
        print(data)
        e = event_form.save()
        return render(request, 'events/checkout.html', context)
      else:
        error_message = 'That time is booked please pick anoter time.'
    event_form = EventForm()
    context = {'event_form': event_form, 'error_message': error_message}
    return render(request, 'events/createEvent.html', context)

def Checkout(request):

    return render(request, 'events/createEvent.html', {
         'event_form': event_form
    })

def random_Tattoo(request):
    if 'randomTat' in request.session:
        rand= request.session['randomTat']
        print(rand)
        context = { 'rand': rand }
    else: 
        rand= random.choice(TattooModel.objects.all())  # filter style & results next
        request.session['randomTat'] = rand.url # pass vars like PHP
        context = { 'rand': request.session['randomTat'], }
    print(context)
    return render(request, 'tattoos/details.html', context)
    # return HttpResponse(f'<img class="randomTat" src="{rand.url}"/>')

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            error_message = 'Invalid credentials - try again'
    else:
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}

    class Meta:
        model = User 
    return render(request, 'registration/signup.html', context)
