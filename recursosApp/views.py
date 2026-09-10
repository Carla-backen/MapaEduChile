from django.shortcuts import render
from .models import RecursoEducativo


def inicio(request):
    recursos = RecursoEducativo.objects.all()

    return render(request, 'recursosApp/inicio.html', {
        'recursos' : recursos

    })