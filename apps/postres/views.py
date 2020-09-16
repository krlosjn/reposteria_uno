from django.shortcuts import render
# Importar vistas genericas
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Instanciar el modelo 'Postres' que se encuentra en la carpeta apps, en models
from apps.postres.models import Postres

#herramientas para direccionar despues de una accion
from django.urls import reverse

#Habilitar el uso de mensajes en django
from django.contrib import messages

#Habilitar mensajes para vistas basadas en clases
from django.contrib.messages.views import SuccessMessageMixin

#Habilitar los formularios en django
from django import forms

# from apps.postres.forms import PostresForm

class PostresListado(ListView):
    model = Postres

class PostreCrear(SuccessMessageMixin, CreateView):
    model = Postres
    form = Postres
    #Me muestra todos los campos de la tabla
    fields = "__all__"
    #Mensaje de confirmacion de guardado exitoso
    success_message = 'Postre creado de manera exitosa'

    #Redireccionar a la pagina principal despues que creamos un registro o postre
    def get_success_url(self):
        return reverse('leer')

class PostreDetalle(DetailView):
    model = Postres

class PostreActualizar(SuccessMessageMixin, UpdateView):
    model = Postres
    form = Postres
    #Me muestra todos los campos de la tabla
    fields = "__all__"
    #Mensaje de confirmacion de actualizacion exitoso
    success_message = 'Postre actualizado de manera exitosa'

    #Redireccionar a la pagina principal despues que creamos un registro o postre
    def get_success_url(self):
        return reverse('leer')

class PostreEliminar(SuccessMessageMixin, DeleteView):
    model = Postres
    form = Postres
     #Me muestra todos los campos de la tabla
    fields = "__all__"

    #Redireccionar a la pagina principal despues que creamos un registro o postre
    def get_success_url(self):
        #Mensaje de confirmacion de eliminacion exitoso
        success_message = 'Postre eliminado de manera exitosa'
        messages.success(self.request,(success_message))
        return reverse('leer')

