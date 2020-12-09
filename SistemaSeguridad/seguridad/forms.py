from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from seguridad.models import Desbloqueo

class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2'] 

class desbloqueoUsuario(forms.ModelForm):
    class Meta:
        model= Desbloqueo
        fields= '__all__'
