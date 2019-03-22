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
        event_form.save(commit=False)
        del event_form.fields['location']
        data = event_form.cleaned_data
        # form.cleaned_data['my_form_field_name']
        print(data)
        e = event_form.save()
        join_data = JoinTable()
        ev = Event.objects.get(id=e.artist)
        l = Location.objects.get(id=e.location)
        art = Artist.objects.get(id=1)
        t = Tattoo.objects.get(id=request.session['tattooId'])

        join_data.event = e.id
        join_data.artist = art.id
        join_data.tattoo = t.id
        join_data.profile = request.user.id
        join_data.location = l.id
        join_data.save()
        appointment = {
            'date': ev.date,
            'time': ev.time
        }
        artist = {
            'name': art.name,
            'phone_number': art.phone_number,
            'email': art.email
        }
        location = {
            'name': l.name,
            'address': l.street,
            'city': l.city
        }
        tattoo = {
            'url': request.session['randomTat'],
            'style': t.style,
            'name': t.name
        }
        context = {
            'appointment': appointment,
            'artist': artist,
            'location': location,
            'tattoo': tattoo
        }
        print(context)
        return render(request, 'events/checkout.html', context)
      else:
        error_message = 'That time is booked please pick anoter time.'
    event_form = EventForm()
    context = {'event_form': event_form, 'error_message': error_message}
    return render(request, 'events/createEvent.html', context)

# def Checkout(request):
#     return render(request, 'events/checkout.html')

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
