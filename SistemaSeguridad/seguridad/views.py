from django.shortcuts import render

# Create your views here.

#Vista de la pagina principal

def index(request):
	return render(request,"seguridad/index.html")

def login(request):
	return render(request,"seguridad/login.html")

def forgot(request):
	return render(request,"seguridad/forgot-password.html")

def primer(request):
	return render(request,"seguridad/primerIngreso.html")
	