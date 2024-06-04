from django.shortcuts import render


# Create your views here.
def register_doctor(request):
    if request.method == 'GET':
        return render(request, 'register_doctor.html')