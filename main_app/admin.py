from django.contrib import admin
from .models import Tattoo, Appointment

# Register your models here.

# Were models already migrated? If so, changing AUTH_USER_MODEL can't be done automatically and requires manual fixing possibly reapplying some migrations
admin.site.register(Tattoo)
admin.site.register(Appointment)
