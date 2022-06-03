from django import forms

class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Profesor_formulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion= forms.CharField(max_length=30)

class Estudiantes_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email= forms.EmailField()
