from django.shortcuts import render
from apps.usuarios.decorators import is_login_redirect


@is_login_redirect('/ticket/listado/')
def home(request):
    return render(request, 'usuarios/login.html', {})