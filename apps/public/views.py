from django.shortcuts import render
from apps.usuarios.decorators import is_login_redirect
from django.contrib.auth.decorators import login_required


@is_login_redirect('/')
def home(request):
    return render(request, 'usuarios/login.html', {})


@login_required
def dashboard(request):
    return render(request, 'base_angular.html', {})