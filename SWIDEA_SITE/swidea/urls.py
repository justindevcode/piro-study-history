from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "swidea"

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name = "create"),
    path('swidea/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('toolhome',views.toolhome, name='toolhome'),
    path('tooldetail/<int:id>',views.tooldetail, name='tooldetail'),
    path('toolcreate', views.toolcreate, name = "toolcreate"),
    path('toolupdate/<int:id>',views.toolupdate, name='toolupdate'),
    path('tooldelete/<int:id>',views.tooldelete, name='tooldelete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)