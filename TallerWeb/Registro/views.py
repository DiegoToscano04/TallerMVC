from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def registro(request):
    return render(request, 'paginas/registro.html')
def Libros(request):
    Libros = Libro.objects.all()
    return render(request, 'Libros/index.html', {'Libros':Libros})
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Libros')
    return render(request, 'Libros/crear.html', {'formulario': formulario})
def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Libros')
    return render(request, 'Libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('Libros')
