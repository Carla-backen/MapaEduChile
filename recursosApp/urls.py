from django.urls import path 
from . import views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('eliminar/<int:id>/', views.eliminar_recurso, name='eliminar_recurso'),
    path("editar/<int:id>/", views.editar_recurso, name="editar_recurso"),
]