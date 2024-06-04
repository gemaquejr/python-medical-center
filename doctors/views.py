from django.shortcuts import render
from .models import Especialidades


# Create your views here.
def register_doctor(request):
    if request.method == 'GET':
        especialidades = Especialidades.objects.all()
        return render(request, 'register_doctor.html', {'especialidades': especialidades})
