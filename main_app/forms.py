from django.forms import ModelForm
from .models import Profile

class Profile(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'password', 'email']