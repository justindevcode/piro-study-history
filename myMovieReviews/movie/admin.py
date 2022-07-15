from django.contrib import admin
from django.shortcuts import redirect
from .models import Movie
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass