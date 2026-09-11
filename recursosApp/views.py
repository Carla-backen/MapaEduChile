from django.shortcuts import render, redirect, get_object_or_404
from .models import RecursoEducativo


def inicio(request):
    recursos = RecursoEducativo.objects.all()

    busqueda = request.GET.get('busqueda')

    if busqueda:
        recursos = recursos.filter(comuna__icontains=busqueda)


    return render(request, 'recursosApp/inicio.html', {
        'recursos' : recursos,
        'busqueda' : busqueda
    })

def eliminar_recurso(request, id):
    recurso = get_object_or_404(RecursoEducativo, id=id)

    if request.method == 'POST':
        recurso.delete()

    return redirect('inicio')

def editar_recurso(request, id):
    recurso = get_object_or_404(RecursoEducativo, id=id)

    if request.method == "POST":
        recurso.nombre = request.POST.get("nombre")
        recurso.descripcion = request.POST.get("descripcion")
        recurso.region = request.POST.get("region")
        recurso.comuna = request.POST.get("comuna")
        recurso.categoria = request.POST.get("categoria")
        recurso.gratuito = request.POST.get("gratuito") == "on"

        recurso.save()

        return redirect("inicio")

    return render(request, "recursosApp/editar_recurso.html", {
    "recurso": recurso
})