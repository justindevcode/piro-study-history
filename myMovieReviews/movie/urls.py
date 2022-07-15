from django.urls import path 
from django.contrib import admin

from . import views

app_name = "movie"

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name = "create"),
    path('movie/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
]