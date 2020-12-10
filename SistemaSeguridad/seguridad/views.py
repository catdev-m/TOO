from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from seguridad.forms import createUserForm
from seguridad.forms import desbloqueoUsuario
from django.contrib.auth.decorators import login_required
from django_otp.decorators import otp_required
# Create your views here.

#Vista de la pagina principal
@otp_required
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


#Esto es parte de lo que debo subir 
def cambiarContra(request):
	return render(request,"seguridad/cambiarContra.html")

def registrar(request):
	form = createUserForm
	
	if request.method=='POST':
		form=createUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Cuenta creada para: ' + user)

			return redirect('login')
	context={'form':form}
	return render(request,"seguridad/register.html",context)

def desbloquear(request):
	form = desbloqueoUsuario
	
	if request.method=='NEW':
		form=desbloqueoUsuario(request.POST)
		if form.is_valid():
			form.save()

	context={'form':form}
	return render(request,"seguridad/desbloquear.html",context)

def mPuestos(request):
	return render(request,"seguridad/mntoPuestos.html")