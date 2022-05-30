
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_coder.models import *
from app_coder.forms import Curso_formulario


# Create your views here.

def inicio(request):

    return render (request, 'index.html')


def cursos(request):

    cursos = Curso.objects.all() #llama a toda la data en la tabla sql
    dicc = {'cursos' : cursos}
    plantilla = loader.get_template('cursos.html')
    documento = plantilla.render(dicc)

    return HttpResponse(documento)


def profesores(request):
    
    profesores = Profesor.objects.all() #llama a toda la data en la tabla sql
    dicc = {'profesores' : profesores}
    plantilla = loader.get_template('profesores.html')
    documento = plantilla.render(dicc)



    return HttpResponse(documento)

def estudiantes(request):
    
    estudiantes = Estudiantes.objects.all() #llama a toda la data en la tabla sql
    dicc = {'estudiantes' : estudiantes}
    plantilla = loader.get_template('estudiantes.html')
    documento = plantilla.render(dicc)



    return HttpResponse(documento)

def entregables(request):
    
    entregables = Entregable.objects.all() #llama a toda la data en la tabla sql
    dicc = {'eentregables' : entregables}
    plantilla = loader.get_template('entregables.html')
    documento = plantilla.render(dicc)



    return HttpResponse(documento)


'''
def alta_curso(request, nombre):

    curso = Curso(nombre = nombre, camada = 287318)
    curso.save()
    texto = f'Se ha guardado en la BD el curso: {curso.nombre}  Camada: {curso.camada}'

    return HttpResponse(texto)
'''

def contacto(request):

    return render(request, 'contacto.html')


def curso_formulario(request):
    
    if request.method == 'POST':

        mi_formulario = Curso_formulario(request.POST) #toma la data tomada del POST

        if mi_formulario.is_valid(): # si lo ingresado es válido
            datos = mi_formulario.cleaned_data # datos del formulario limpios (diccionario)
       
        curso = Curso(nombre=datos['nombre'], camada=datos['camada'])
        curso.save()
   
        return render (request, 'formulario.html')

    return render(request, 'formulario.html')


def buscar_curso(request):

    return render(request, 'buscar_curso.html')

def buscar(request):

    if request.GET['nombre']:

        #respuesta = f"Estamos buscando los cursos de: {request.GET['nombre']}"
        nombre=request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)   
        return render(request, 'resultado_busqueda.html', {'cursos':cursos})

    else:
        HttpResponse('Datos ingresados no validos')



'''

def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST['nombre'], camada=request.POST['camada'])
        curso.save()
        return render (request, 'formulario.html')

    return render(request, 'formulario.html')
    
    '''