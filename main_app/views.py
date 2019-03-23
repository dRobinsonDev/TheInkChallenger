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
from .getContext import *
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
def event_checkout(request):
    # updating event_checkout  to DRY code
    return render(request, 'tattoos')


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
            rand = json.loads(rand)
            url = rand[0]['fields']['url']
            url = str(url)
            context = { 'rand': url}
            return render(request, 'tattoos/details.html', context)
        else: 
            rand = random.choice(Tattoo.objects.all())
            rand = serializers.serialize("json", [rand])
            rand = json.loads(rand)
            request.session['randomTat'] = rand
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
