from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
def is_doctor(user):
    return DadosMedico.objects.filter(user=user).exists()


class Especialidades(models.Model):
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.especialidade


class DadosMedico(models.Model):
    crm = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    rg = models.ImageField(upload_to='rgs')
    cedula_identidade_medica = models.ImageField(upload_to='cim')
    foto = models.ImageField(upload_to='fotos_perfil')
    descricao = models.TextField()
    valor_consulta = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

    @property
    def proxima_consulta(self):
        proxima_consulta = SetDate.objects.filter(user=self.user).filter(data__gt=datetime.now()).filter(agendado=False).order_by('data').first()
        return proxima_consulta


class SetDate(models.Model):
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    agendado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.data)
