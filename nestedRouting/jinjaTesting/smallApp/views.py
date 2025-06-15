from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def smallApp(request):
    current_time = timezone.now()
    return render(request, 'smallApp.html', {'current_time': current_time})

def order(request):
      current_time = timezone.now()
      return render(request, 'order.html', {'current_time': current_time})