from django.db import models
from django.utils import timezone

# Create your models here.
class user(models.Model):
   USER_TYPE = [
      ('admin', 'Admin'),
      ('user', 'User'),
   ]
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=254, unique=True)
   profile = models.ImageField(upload_to='profile_pics/')
   date = models.DateTimeField(default=timezone.now)
   user_type = models.CharField(max_length=10, choices=USER_TYPE, default='user')
   
   def __str__(self):
      return self.name