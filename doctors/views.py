from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico, is_doctor, SetDate
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime, timedelta
from patients.models import Consultation


# Create your views here.
def register_doctor(request):

    if is_doctor(request.user):
        messages.add_message(request, constants.WARNING, 'Você já é um médico cadastrado!')
        return redirect('/doctors/consultation_time')

    if request.method == 'GET':
        especialidades = Especialidades.objects.all()
        return render(request, 'register_doctor.html', {'especialidades': especialidades})
    elif request.method == 'POST':
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        endereco = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            endereco=endereco,
            bairro=bairro,
            numero=numero,
            rg=rg,
            cedula_identidade_medica=cim,
            foto=foto,
            especialidade_id=especialidade,
            descricao=descricao,
            valor_consulta=valor_consulta,
            user=request.user
        )

        dados_medico.save()

        messages.add_message(request, constants.SUCCESS, 'Médico cadastrado com sucesso!')
        return redirect('/doctors/consultation_time')


def available_dates(request):

    if not is_doctor(request.user):
        messages.add_message(request, constants.WARNING, 'Você não é um médico cadastrado!')
        return redirect('/users/logout')

    if request.method == 'GET':
        dados_medico = DadosMedico.objects.get(user=request.user)
        datas_abertas = SetDate.objects.filter(user=request.user)
        return render(request, 'available_dates.html', {'dados_medico': dados_medico, 'datas_abertas': datas_abertas})
    elif request.method == 'POST':
        data = request.POST.get('data')
        data_formatada = datetime.strptime(data, '%Y-%m-%dT%H:%M')

        if data_formatada <= datetime.now():
            messages.add_message(request, constants.WARNING, 'A data não pode ser anterior a data atual!')
            return redirect('/doctors/available_dates')

        abrir_horario = SetDate(
            data=data_formatada,
            user=request.user,
        )

        abrir_horario.save()

        messages.add_message(request, constants.SUCCESS, 'Horário cadastrado com sucesso!')
        return redirect('/doctors/available_dates')


def medical_consultations(request):
    if not is_doctor(request.user):
        messages.add_message(request, constants.WARNING, 'Você não é um médico cadastrado!')
        return redirect('/users/logout')

    hoje = datetime.now().date()
    consultas_hoje = Consultation.objects.filter(data_aberta__user=request.user).filter(data_aberta__data__gte=hoje).filter(data_aberta__data__lt=hoje + timedelta(days=1))
    consultas_restantes = Consultation.objects.exclude(id__in=consultas_hoje.values('id'))

    return render(request, 'medical_consultations.html', {'consultas_hoje': consultas_hoje, 'consultas_restantes': consultas_restantes})
