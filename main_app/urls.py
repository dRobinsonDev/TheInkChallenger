from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('about/', views.Ab   out.as_view(), name="about"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('artists/', views.ArtistList.as_view(), name="artists"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('events/', views.Create_Event, name='events'),
    path('events/checkout', views.Checkout, name='checkout'),
    path('shops/', views.ShopList.as_view(), name="shops"),
    path('tattoos/', views.TattooList.as_view(), name="tattoos"),
    path('tattoos/appointment', views.Create_Event, name="appointments"),
    path('tattoos/random', views.random_Tattoo, name="random_tattoo"),
]


# These are the paths the django.contrib.auth.urls has added
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/done/ [name='password_reset_complete']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']