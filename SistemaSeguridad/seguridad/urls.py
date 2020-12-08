from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, forgot, primer, registrar, login
app_name='seguridad'

urlpatterns = [
   path('',login, name='login') 
]

seguridad_patterns =[
	path('index.html/', index, name='login'),
	#path('login.html/',login,name='login'),
	path('forgot-password',forgot,name='forgot'),
	path('index.html/',index,name='index'),
	path('primerIngreso.html/',primer,name='primer'),
	path('register.html/',registrar,name='registrar'),
	#Desde acá comienzo para agregar
	path('reset_password/',
	auth_views.PasswordResetView.as_view(template_name="seguridad/forgot-password.html"),
	name="reset_password"),

	path('reset_password_sent/',
	auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
	name="password_reset_done"),

#Hasta acá	
]