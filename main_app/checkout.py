@login_required
def Create_Event(request):
    error_message = ''
    try:
        user = JoinTable.objects.get(profile=request.user.id)
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
            return render('events/checkout.html', context)
    except:
            context = {}
    
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save(commit=False)
            del event_form.fields['location']
            data = event_form.cleaned_data
            e = event_form.save()
            join_data = JoinTable()
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
                print(context)
        else:
            error_message = "Sorry that time is booked. Please pick another time."
            context = {'error_message': error_message}
