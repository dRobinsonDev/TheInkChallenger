from django.core import serializers
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
import json
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .getContext import *
from .forms import *
from .models import User, Artist, Location, Tattoo as TattooModel, Appointment, Profile, Photo
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
def event_checkout(request):
    # updating event_checkout  to DRY code
    tattoo_message = ''
    error_message = ''
    event_form = EventForm()
    try:
        if JoinTable.objects.filter         (profile=request.user.id):
            tattoo_message = 'Sorry you have already participated in the Ink Challenge.'
            print('working first')
    except:
        pass
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            data = event_form.cleaned_data
            e = event_form.save()
            ev = Event.objects.get(id=e.id)
            l = Location.objects.get(id=e.location)
            art = Artist.objects.get(id=e.artist)

            t = Tattoo.objects.get(id=request.session['tattooId'])
            join_data = JoinTable()
            join_data.appointment = e.id
            join_data.artist = art.id
            join_data.tattoo = t.id
            join_data.profile = request.user.id
            join_data.location = l.id
            join_data.save()
            t.available = False
            t.save()
            print(join_data)
            context = getUserContext(request, request.user.id)
            return render(request, 'events/checkout.html', context)


    if 'randomTat' in request.session:
            tattoo = request.session.get('randomTat')
            try:
                tattoo = json.loads(tattoo)
                tattoo = tattoo[0]['fields']['url']
            except:
                tattoo = tattoo[0]['fields']['url']
    else:
        return render('tattoos/random')
    context = {
        'error_message': error_message,
        'tattoo_message': tattoo_message,
        'event_form': event_form,
        'tattoo': tattoo,
    }
    print('working last')
    return render(request, 'events/createEvent.html', context)


@login_required
def random_Tattoo(request):
        try:
            if len(JoinTable.objects.all()) > 0:
                try:
                    if JoinTable.objects.get(profile=request.user.id):
                        rand = JoinTable.objects.get(profile=request.user.id)
                        url = Tattoo.objects.all()[rand.tattoo].url
                except:
                    pass
        except:
            context = { 'rand': rand }
            return render(request, 'tattoos/details.html', context)
        if 'randomTat' in request.session:
            rand = request.session.get('randomTat')
            try:
                rand = json.loads(rand)
                url = rand[0]['fields']['url']
            except:
                url = rand[0]['fields']['url']
            url = str(url)
            request.session['tattooId'] = rand[0]['pk']
            context = { 'rand': url}
            return render(request, 'tattoos/details.html', context)
        else: 
            rand = random.choice(Tattoo.objects.filter(available=True))
            rand = serializers.serialize("json", [rand])
            rand = json.loads(rand)
            request.session['randomTat'] = rand
            request.session['tattooId'] = rand[0]['pk']

            context = {'rand': rand[0]['fields']['url']}
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
def event_payment(request):
    print(request, 'hello')
    context = {}
    context = getUserContext(request, request.user.id)

    return render(request, 'events/checkout.html', context)