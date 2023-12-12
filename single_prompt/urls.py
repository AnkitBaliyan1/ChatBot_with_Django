from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('oneliner/', views.input_view, name='single'),
    path('translate/', views.translate_view, name='translator'),
    path('response', views.chat_view, name="chat"),
    path('bulkfile/', views.bulkfile, name='bulk'),
]