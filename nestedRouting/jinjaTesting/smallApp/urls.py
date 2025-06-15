from django.urls import path
from . import views

# localhost:8000/smallApp/
urlpatterns = [
      path('', views.smallApp, name='smallApp'),
      path('order/', views.order, name='order'),
]
