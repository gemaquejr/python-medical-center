from django.shortcuts import render
from doctors.models import DadosMedico, Especialidades, SetDate
from datetime import datetime


# Create your views here.
def home(request):
    if request.method == "GET":
        medico_filtrar = request.GET.get('medico')
        especialidades_filtrar = request.GET.getlist('especialidades')
        medicos = DadosMedico.objects.all()

        if medico_filtrar:
            medicos = medicos.filter(nome__icontains=medico_filtrar)

        if especialidades_filtrar:
            medicos = medicos.filter(especialidade_id__in=especialidades_filtrar)

        especialidades = Especialidades.objects.all()
        return render(request, 'home.html', {'medicos': medicos, 'especialidades': especialidades})


def choose_date(request, id_dados_medicos):
    if request.method == "GET":
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        datas_abertas = SetDate.objects.filter(user=medico.user).filter(data__gte=datetime.now()).filter(agendado=False)
        return render(request, 'choose_date.html', {'medico': medico, 'datas_abertas': datas_abertas})
