from django.contrib import admin

# Register your models here.
from .models import swidea, swtool

@admin.register(swidea)
class SwideaAdmin(admin.ModelAdmin):
    pass

@admin.register(swtool)
class SwtoolAdmin(admin.ModelAdmin):
    pass