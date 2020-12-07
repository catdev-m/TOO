from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.

#Vista de la pagina principal

def index(request):
	return render(request,"seguridad/index.html")

def login(request):
	return render(request,"registration/login.html")


def forgot(request):
	return render(request,"seguridad/forgot-password.html")

def primer(request):
	return render(request,"seguridad/primerIngreso.html")

def registrar(request):
	return render(request,"seguridad/register.html")

