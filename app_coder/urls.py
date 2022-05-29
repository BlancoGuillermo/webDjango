from multiprocessing.spawn import import_main_path
from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='Inicio'),
    path('alta_curso/<nombre>' , views.alta_curso), #<nombre> pide parámetro
    path('cursos' , views.cursos, name='Cursos'),
    path('profesores', views.profesores, name='Profesores'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('entregables', views.entregables, name='Entregables'),
    path('contacto', views.contacto)

]