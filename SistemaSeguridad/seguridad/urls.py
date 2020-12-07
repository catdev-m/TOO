from django.urls import path
#from django.contrib.auth.models import User
from .views import index, forgot, primer, registrar, login


urlpatterns = [
   path('',login, name='login') 
]

seguridad_patterns =[
	path('index.html/', index, name='login'),
	#path('login.html/',login,name='login'),
	path('forgot-password.html/',forgot,name='forgot'),
	path('index.html/',index,name='index'),
	path('primerIngreso.html/',primer,name='primer'),
	path('register.html/',registrar,name='registrar'),
]