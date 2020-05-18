from django import forms
from frth_app.models import User_Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class User_ProfileForm(forms.ModelForm):
    class Meta():
        model = User_Profile
        fields = ('port_folio','picture')
