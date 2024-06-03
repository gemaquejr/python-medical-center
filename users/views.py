from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


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
            print('Senhas não conferem')
            return redirect('register')

        if len(senha) < 6:
            print('Senha muito curta')
            return redirect('register')

        users = User.objects.filter(username=username)
        print(users.exists())

        if users.exists():
            print('Usuário já existe')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        return HttpResponse(f'Usuário cadastrado com sucesso.')
