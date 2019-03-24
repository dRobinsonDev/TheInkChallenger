from .models import *

def getUserContext(request, userNum):
    user = JoinTable.objects.get(profile=userNum)
    ev = Event.objects.get(id=user.appointment)
    l = Location.objects.get(id=user.location)
    art = Artist.objects.get(id=user.artist)
    t = Tattoo.objects.get(id=request.session['tattooId'])
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
        'url': t.url,
        'style': t.style,
        'name': t.name
    }
    context = {
        'appointment': appointment,
        'artist': artist,
        'location': location,
        'tattoo': tattoo
    }
    return context

def getContext(request, POST):
    print(POST)
    l = Location.objects.get(id=POST.get("location"))
    art = Artist.objects.get(id=POST.get("artist"))
    t = Tattoo.objects.get(id=request.session['tattooId'])
    appointment = {
        'date': POST.get('day'),
        'time': POST.get('start_time')
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
        'url': t.url,
        'style': t.style,
        'name': t.name
    }
    context = {
        'appointment': appointment,
        'artist': artist,
        'location': location,
        'tattoo': tattoo
    }
    return context