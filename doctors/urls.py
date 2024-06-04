from django.urls import path
from . import views


urlpatterns = [
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('available_dates/', views.available_dates, name='available_dates')
]
