from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_coder.models import Curso
# Create your views here.

def cursos(request):

    cursos = Curso.objects.all() #llama a toda la data en la tabla sql
    dicc = {'cursos' : cursos}
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render(dicc)



    return HttpResponse(documento)


def alta_curso(request, nombre):

    curso = Curso(nombre = nombre, camada = 287318)
    curso.save()
    texto = f'Se ha guardado en la BD el curso: {curso.nombre}  Camada: {curso.camada}'

    return HttpResponse(texto)