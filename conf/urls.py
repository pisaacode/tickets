"""tickes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.views.generic import TemplateView
from apps.public.views import home, dashboard

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ticket/', include('apps.soporte.urls')),
    url(r'^usuarios/', include('apps.usuarios.urls')),
    url(r'^home', home),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/ticket/', include('apps.soporte.url_api')),
    url(r'^.*', dashboard, name='dashboard'),
]
