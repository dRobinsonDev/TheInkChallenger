from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('artists/', views.Artist.as_view(), name="artists"),
    path('tattoos/', views.Tattoo.as_view(), name="tattoos"),
    path('tattoos/appointments/', views.Appointment.as_view(), name="appointments"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]