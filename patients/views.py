from django.shortcuts import render
from doctors.models import DadosMedico


# Create your views here.
def home(request):
    if request.method == "GET":
        medicos = DadosMedico.objects.all()
        return render(request, 'home.html', {'medicos': medicos})
