"""Define los patrones url para la aplicación accounts"""
from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    #Incluimos las rutas auth por defecto
    path('',include('django.contrib.auth.urls')),
    #Página de registro de usuarios
    path('register/',views.register, name = 'register'),
]
