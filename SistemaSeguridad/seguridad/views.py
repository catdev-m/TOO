from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

#Vista de la pagina principal

def index(request):
	return render(request,"seguridad/index.html")

def login(request):
	return render(request,"registration/login.html")


def forgot(request):
	if request.method=="POST":
		subject=request.POST["correo"]
		email_from=settings.EMAIL_HOST_USER
		recipient_list=["csystem205@gmail.com",subject]
		send_mail('Recupere su contraseña','Recupere su contraseña ',email_from,recipient_list)
		
		return render(request,"seguridad/forgot-password.html")
	return render(request,"seguridad/forgot-password.html")

def primer(request):
	return render(request,"seguridad/primerIngreso.html")

def registrar(request):
	return render(request,"seguridad/register.html")

