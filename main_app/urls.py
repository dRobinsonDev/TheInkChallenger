from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('tattoos/artists/', views.Artist.as_view(), name="artists"),
    path('accounts/', include('django.contrib.auth.urls')),

]