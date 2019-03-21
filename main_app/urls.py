from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('about/', views.About.as_view(), name="about"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('artists/', views.ArtistList.as_view(), name="artists"),
    path('shops/', views.ShopList.as_view(), name="shops"),
    path('tattoos/', views.TattooList.as_view(), name="tattoos"),
    path('tattoos/appointment', views.Appointment.as_view(), name="appointments"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]


# These are the paths the django.contrib.auth.urls has added
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']