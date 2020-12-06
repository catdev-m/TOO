from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def forgot(request):
    return render(request,"blogapp/static/forgot-password.html")
