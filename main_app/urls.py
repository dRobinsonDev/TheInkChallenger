from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('artists/', views.ArtistList.as_view(), name="artists"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('events/', views.event_checkout, name='event_checkout'),
    path('events/checkout', views.event_checkout, name='event_checkout'),
    path('shops/', views.ShopList.as_view(), name="shops"),
    path('tattoos/', views.TattooList.as_view(), name="tattoos"),
    path('tattoos/random', views.random_Tattoo, name="random_tattoo"),
]