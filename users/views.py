from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As Senhas não conferem')
            return redirect('register')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A Senha deve ter pelo menos 6 caracteres')
            return redirect('register')

        users = User.objects.filter(username=username)
        print(users.exists())

        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existente')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        return HttpResponse(f'Usuário cadastrado com sucesso.')


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
