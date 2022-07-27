from django.contrib import admin
from django.urls import path
from . import views

appname = 'pirostagram'

urlpatterns = [
    path('', views.home, name='home'),
    path('content_ajax/', views.content_ajax, name = 'content_ajex'),
    path('like_ajax/', views.like_ajax, name = 'like_ajex'),
    path('delete_ajax/', views.delete_ajax, name='delete_ajax')

]