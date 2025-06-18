from django.shortcuts import render
from django.http import HttpResponse
from .models import user

# Create your views here.

def home(request):
    return render(request, 'smallApp/home.html')

def testing(request):
   users = user.objects.all()
   context = {
       'users': users
   }
   return render(request, 'smallApp/testing.html', context)