from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('choose_date/<int:id_dados_medicos>', views.choose_date, name="choose_date"),
    path('choose_time/<int:id_data_aberta>', views.choose_time, name="choose_time")
]
