from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        usernane = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            print('Senhas não conferem')
            return redirect('register')

        if len(senha) < 6:
            print('Senha muito curta')
            return redirect('register')

        return HttpResponse('Usuário cadastrado com sucesso')
