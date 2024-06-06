from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('choose_date/<int:id_dados_medicos>', views.choose_date, name="choose_date")
]
