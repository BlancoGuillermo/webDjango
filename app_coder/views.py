from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_coder.models import Curso
# Create your views here.

def inicio(request):

    plantilla = loader.get_template('index.html')
    documento = plantilla.render(plantilla)



    return HttpResponse(documento)




def cursos(request):

    cursos = Curso.objects.all() #llama a toda la data en la tabla sql
    dicc = {'cursos' : cursos}
    plantilla = loader.get_template('cursos.html')
    documento = plantilla.render(dicc)

    return HttpResponse(documento)


def profesores(request):
    
    plantilla = loader.get_template('profesores.html')
    documento = plantilla.render(plantilla)



    return HttpResponse(documento)

def estudiantes(request):
    
    plantilla = loader.get_template('estudiantes.html')
    documento = plantilla.render(plantilla)



    return HttpResponse(documento)

def entregables(request):
    
    plantilla = loader.get_template('entregables.html')
    documento = plantilla.render(plantilla)



    return HttpResponse(documento)










def alta_curso(request, nombre):

    curso = Curso(nombre = nombre, camada = 287318)
    curso.save()
    texto = f'Se ha guardado en la BD el curso: {curso.nombre}  Camada: {curso.camada}'

    return HttpResponse(texto)

