"""
URL configuration for SocialMediaClone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from groups import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroup.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<str:slug>/', views.SingleGroup.as_view(), name='single'),
    path('join/<str:slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<str:slug>/', views.LeaveGroup.as_view(), name='leave'),
]
