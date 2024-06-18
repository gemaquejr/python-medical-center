from django.shortcuts import render, redirect
from doctors.models import DadosMedico, Especialidades, SetDate
from datetime import datetime
from .models import Consultation
from django.contrib import messages
from django.contrib.messages import constants


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


def choose_time(request, id_data_aberta):
    if request.method == "GET":
        data_aberta = SetDate.objects.get(id=id_data_aberta)
        horario_agendado = Consultation(
            paciente=request.user,
            data_aberta=data_aberta
        )

        horario_agendado.save()

        data_aberta.agendado = True
        data_aberta.save()

        messages.add_message(request, constants.SUCCESS, 'Consulta agendada com sucesso')

        return redirect('/patients/my_consultations')


def my_consultations(request):
    minhas_consultas = Consultation.objects.filter(paciente=request.user).filter(data_aberta__data__gte=datetime.now())
    return render(request, 'my_consultations.html', {'minhas_consultas': minhas_consultas})
