from django.shortcuts import render
from django.http import HttpResponse
from.models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def Libros(request):
    Libros = Libro.objects.all()
    return render(request, 'Libros/index.html', {'Libros':Libros})
def crear(request):
    formulario = LibroForm(request.POST or None)
    return render(request, 'Libros/crear.html', {'formulario': formulario})
def editar(request):
    return render(request, 'Libros/editar.html')

