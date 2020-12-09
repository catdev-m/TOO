from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, forgot, primer, registrar, login, desbloquear
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

	#Esto quizás lo deba subir al nuevo pero no sirven realmente no se si se necesitan
	path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="seguridad/cambiarContra.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_form.html"), 
        name="password_reset_complete"),


#Hasta acá	
#nueva vista crear usuario 
	path('registrar',registrar,name='registrar'),
	path('desbloquear',desbloquear,name='desbloquear'),
	
]