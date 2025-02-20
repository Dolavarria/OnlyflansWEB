"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views 
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from web.views import indice,about,welcome,contacto,contacto_exito

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('ubicacion/', include('web.urls')),
    path('',indice,name="indice"),
    path('about/',about,name='about'),
    path('welcome/',welcome,name="welcome"),
    path('contacto/',contacto,name="contacto"),
    path('contacto/exito/',contacto_exito, name="contacto_success"), 
    path('admin/', admin.site.urls),

    ]
