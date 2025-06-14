from django.contrib import admin
from django.urls import path
from firstPageDjango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('skills/', views.skills, name='skills'),
path('experience/', views.experience, name='experience'),
    path('resume/', views.resume, name='resume'),
]

