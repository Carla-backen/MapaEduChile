from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import RecursoEducativo, Comuna, Categoria


# =========================================
# PÁGINA PRINCIPAL
# =========================================

def inicio(request):
    recursos = RecursoEducativo.objects.all()

    busqueda = request.GET.get('busqueda', '').strip()

    if busqueda:
        recursos = recursos.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(comuna__nombre__icontains=busqueda) |
            Q(comuna__region__nombre__icontains=busqueda) |
            Q(categoria__nombre__icontains=busqueda)
        ).distinct()

    return render(request, 'recursosApp/inicio.html', {
        'recursos': recursos,
        'busqueda': busqueda
    })


# =========================================
# AGREGAR RECURSO
# =========================================

def agregar_recurso(request):
    comunas = Comuna.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        comuna_id = request.POST.get('comuna')
        categoria_id = request.POST.get('categoria')

        direccion = request.POST.get('direccion', '')
        sitio_web = request.POST.get('sitio_web', '')

        gratuito = request.POST.get('gratuito') == 'on'

        comuna = get_object_or_404(
            Comuna,
            id=comuna_id
        )

        categoria = get_object_or_404(
            Categoria,
            id=categoria_id
        )

        RecursoEducativo.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            comuna=comuna,
            categoria=categoria,
            direccion=direccion,
            sitio_web=sitio_web,
            gratuito=gratuito
        )

        return redirect('inicio')

    return render(request, 'recursosApp/agregar_recurso.html', {
        'comunas': comunas,
        'categorias': categorias
    })


# =========================================
# ELIMINAR RECURSO
# =========================================

def eliminar_recurso(request, id):
    recurso = get_object_or_404(
        RecursoEducativo,
        id=id
    )

    if request.method == 'POST':
        recurso.delete()

    return redirect('inicio')


# =========================================
# EDITAR RECURSO
# =========================================

def editar_recurso(request, id):
    recurso = get_object_or_404(
        RecursoEducativo,
        id=id
    )

    comunas = Comuna.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':

        recurso.nombre = request.POST.get('nombre')
        recurso.descripcion = request.POST.get('descripcion')

        comuna_id = request.POST.get('comuna')
        categoria_id = request.POST.get('categoria')

        recurso.comuna = get_object_or_404(
            Comuna,
            id=comuna_id
        )

        recurso.categoria = get_object_or_404(
            Categoria,
            id=categoria_id
        )

        recurso.direccion = request.POST.get(
            'direccion',
            ''
        )

        recurso.sitio_web = request.POST.get(
            'sitio_web',
            ''
        )

        recurso.gratuito = (
            request.POST.get('gratuito') == 'on'
        )

        recurso.save()

        return redirect('inicio')

    return render(request, 'recursosApp/editar_recurso.html', {
        'recurso': recurso,
        'comunas': comunas,
        'categorias': categorias
    })