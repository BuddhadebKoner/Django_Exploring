from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def home(request):
    """
    Render the home page with the current date and time.
    """
    current_time = timezone.now()
    return render(request, 'home.html', {'current_time': current_time})