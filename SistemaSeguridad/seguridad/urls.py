from django.urls import path


from .views import index, login, forgot, primer 


urlpatterns = [
    path('', index),
]

seguridad_patterns =[
	path('login.html/',login,name='login'),
	path('forgot-password.html/',forgot,name='forgot'),
	path('index.html/',index,name='index'),
	path('primerIngreso.html/',primer,name='primer'),

]