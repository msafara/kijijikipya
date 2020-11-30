from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html', views.about, name="about"), 
    path('blog.html', views.blog, name="blog"),
    path('projects.html', views.projects, name="projects"),
    path('whatwedo.html', views.whatwedo, name="whatwedo"),
    path('contact.html', views.contact, name= "contact"),
]
