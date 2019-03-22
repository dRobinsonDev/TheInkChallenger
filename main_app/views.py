from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import json
import random
from .models import User, Artist, Location, Tattoo as TattooModel, Appointment, Profile, Photo
from .forms import *
from .utils import *



# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {'data': 'data'}
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

@login_required
def Create_Event(request):
    error_message = ''
    try:
        user = JoinTable.objects.get(profile=request.user.id)
        print('User has a tat')
        if user > 0 and user != None:
            ev = Event.objects.get(id=user.appointment)
            l = Location.objects.get(id=user.location)
            art = Artist.objects.get(id=user.artist)
            t = Tattoo.objects.get(id=user.tattoo)

            appointment = {
                'date': ev.day,
                'time': ev.start_time
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
            return render(request, 'events/checkout.html', context)
    except:
        print('No user tattoo')
        context = {}
    
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save(commit=False)
            del event_form.fields['location']
            data = event_form.cleaned_data
            e = event_form.save()
            join_data = JoinTable()
            print('table created')
            try:
                print('table exists alrdy')
                if JoinTable.objects.get(profile=request.user.id):
                    user = JoinTable.objects.get(profile=request.user.id)
                    ev = Event.objects.get(id=user.appointment)
                    l = Location.objects.get(id=user.location)
                    art = Artist.objects.get(id=user.artist)
                    t = Tattoo.objects.get(id=request.session['tattooId'])
                    join_data.appointment = user.appointment
                    join_data.artist = user.artist
                    join_data.tattoo = user.tattoo
                    join_data.profile = request.user.id
                    join_data.location = l.id
                    join_data.save()
                    appointment = {
                        'date': ev.day,
                        'time': ev.start_time
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
                else:
                    print('create new relation entry')
                    ev = Event.objects.get(id=e.appointment)
                    l = Location.objects.get(id=e.location)
                    art = Artist.objects.get(id=e.artist)
                    t = Tattoo.objects.get(id=request.session['tattooId'])
                    join_data.appointment = e.id
                    join_data.artist = art.id
                    join_data.tattoo = t.id
                    t.available = False
                    t.save()
                    join_data.profile = request.user.id
                    join_data.location = l.id
                    join_data.save()
                    appointment = {
                        'date': ev.day,
                        'time': ev.start_time
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
                    print(context, hello)
            except:
                pass
        else:
            error_message = "Sorry that time is booked. Please pick another time."
            context = {'error_message': error_message}

        print(context)
        return render(request, 'tattoos/details.html', context)
    else:
        event_form = EventForm()
        context = {'event_form': event_form, 'error_message': error_message}
        return render(request, 'events/createEvent.html', context)
@login_required
def event_checkout(request):
    error_message = ''
    if 'randomTat' in request.session:
        error_message = request.session['randomTat']
    
    if request.method == "POST":
      event_form = EventForm(request.POST)
      if event_form.is_valid():
        data = event_form.cleaned_data
        e = event_form.save()
        join_data = JoinTable()
        if JoinTable.objects.filter(profile=request.user.id):
            user = JoinTable.objects.get(profile=request.user.id)
            ev = Event.objects.get(id=user.appointment)
            l = Location.objects.get(id=user.location)
            art = Artist.objects.get(id=user.artist)
            t = Tattoo.objects.get(id=request.session['tattooId'])
            join_data.appointment = user.appointment
            join_data.artist = user.artist
            join_data.tattoo = user.tattoo
            join_data.profile = request.user.id
            join_data.location = l.id
            join_data.save()
            appointment = {
                'date': ev.day,
                'time': ev.start_time
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
                'url': t.tattoo,
                'style': t.style,
                'name': t.name
            }
            context = {
                'appointment': appointment,
                'artist': artist,
                'location': location,
                'tattoo': tattoo
            }
            return render(request, 'events/checkout.html', context)
      else:
        e = event_form.save()
        error_message = 'That time is booked please pick anoter time.'
        ev = Event.objects.get(id=e.appointment)
        l = Location.objects.get(id=e.location)
        art = Artist.objects.get(id=e.artist)
        t = Tattoo.objects.get(id=request.session['tattooId'])
        join_data.appointment = e.id
        join_data.artist = art.id
        join_data.tattoo = t.id
        t.available = False
        t.save()
        join_data.profile = request.user.id
        join_data.location = l.id
        join_data.save()
        appointment = {
            'date': ev.day,
            'time': ev.start_time
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
    else:
        event_form = EventForm()
        context = {'event_form': event_form, 'error_message': error_message}
        return render(request, 'events/createEvent.html', context)


@login_required
def random_Tattoo(request):
        try:
            if len(JoinTable.objects.all()) > 0:
                try:
                    if JoinTable.objects.get(profile=request.user.id):
                        rand = JoinTable.objects.get(profile=request.user.id)
                        url = Tattoo.objects.all()[rand.tattoo].url
                        print('im here')
                except:
                    pass
        except:
            context = { 'rand': rand }
            print(context)
            return render(request, 'tattoos/details.html', context)
        if 'randomTat' in request.session:
            rand = request.session.get('randomTat')
            rand = json.loads(rand)
            url = rand[0]['fields']['url']
            print(url, 'hello')
            url = str(url)
            context = { 'rand': url}
            return render(request, 'tattoos/details.html', context)
        else: 
            rand = random.choice(Tattoo.objects.all())
            rand = serializers.serialize("json", [rand])
            request.session['randomTat'] = rand
            context = {'rand': rand.url}
            print('last')
            return render(request, 'tattoos/details.html', context)

def signup(request):
    error_message = ''
    context = {}
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
