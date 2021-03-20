from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import render

def user_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        error = {}
        if user:
            login(request, user)
            return redirect('listado_ticket')
        else:
            error = 'Datos incorrectos intente de nuevo'

    ctx = {
        'error': error
    }
    return render(request, 'usuarios/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('/home')