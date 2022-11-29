from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from mvt.models import *
from django.shortcuts import render
from MVT_MarkoMihocevich.templates import *
from mvt.models import Curso
from mvt.forms import *


def index(request):
    entries = Alumno.objects.all()
    context = {'entries': entries}
    return render(request, 'index.html', context)   


def cursos(request):
    return render(request, "cursoss.html")

def inicio(request):
    return render(request, "inicio.html")    


def creacion_curso(request):

    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]

        curso = Curso(nombre = nombre_curso, camada = numero_camada)
        curso.save()

    return render(request, "curso_formulario.html")


def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

            #validamos que el form este ok
        if formulario.is_valid():
           #recuperamos la info ok
            data = formulario.cleaned_data


            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            
            profesor.save()
    
               
    
    formulario = ProfesorFormulario()
    contexto = {"formulario": formulario}
    return render(request, "profesores_formularios.html", contexto)




def buscar_curso(request):    

    return render(request, "busqueda_cursos.html")



def resultado_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)

    return render(request, "resultados_busquedas_cursos.html", {"cursos": cursos})
    




def creacion_alumnos(request):

    if request.method == "POST":
        formulario = AlumnosFormulario(request.POST)

            #validamos que el form este ok
        if formulario.is_valid():
           #recuperamos la info ok
            data = formulario.cleaned_data


            alumnos = Alumno(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            
            alumnos.save()

    formulario = AlumnosFormulario()
    contexto = {"formulario": formulario}
    return render(request, "alumnos_formularios.html", contexto)

