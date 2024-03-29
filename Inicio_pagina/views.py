from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Formulario, FormularioPersonas
from .forms import FormularioForm, FormularioPersonasForm
from django.core.mail import send_mail
from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import mimetypes
import smtplib
import base64
from django.core.mail import EmailMessage
import tempfile
import shutil
import subprocess
from django.core.mail import EmailMessage



def inicio(request):
    return render(request, 'home.html')


def productos(request):
    return render(request, 'Inicio/productos.html')


def soluciones(request):
    return render(request, 'Inicio/soluciones.html')


def contacto(request):
    if request.method == 'POST':
        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Envía el correo electrónico
            enviar_correo(formulario.cleaned_data)
            return redirect('confirmacion')
    else:
        formulario = FormularioForm()
    return render(request, 'Inicio/contacto.html', {'formulario': formulario})


def enviar_correo(datos_formulario):
    asunto = 'Nueva solicitud de contacto'
    mensaje = f'Nombre: {datos_formulario["nombre"]}\n' \
              f'Empresa: {datos_formulario["empresa"]}\n' \
              f'Teléfono: {datos_formulario["telefono"]}\n' \
              f'Email: {datos_formulario["email"]}\n' \
              f'Motivo de contacto: {datos_formulario["motivo_contacto"]}\n' \
              f'Forma de contacto preferida: {datos_formulario["forma_contacto"]}'
    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,
        ['informaticakyvm@gmail.com'],
        fail_silently=False,
    )


def confirmacion(request):
    return render(request, 'Inicio/confirmacion_formulario.html')


def form_personas(request):
    if request.method == 'POST':
        formulario = FormularioPersonasForm(request.POST, request.FILES)
        if formulario.is_valid():
            # No es necesario guardar el formulario en la base de datos
            # Obtener el archivo adjunto del formulario con el nombre correcto del campo
            archivo_adjunto = request.FILES.get('cv')
            if archivo_adjunto:
                # Envía correo para trabajadores solo si se adjunta un archivo
                enviar_correo_trabajadores(formulario.cleaned_data, archivo_adjunto)
            else:
                print("No se adjuntó ningún archivo.")
            return redirect('confirmacion_2')
    else:
        formulario = FormularioPersonasForm()
    return render(request, 'Inicio/form_personas.html', {'formulario': formulario})


def enviar_correo_trabajadores(datos_formulario, archivo_adjunto):
    # Definir las opciones de interés
    opciones_interes = {
        'Programacion': 'Programación',
        'Gestion_proyectos': 'Gestión de Proyectos',
        'Soporte_tecnico': 'Soporte técnico',
        'Testing': 'Testing',
        'Arquitecto_soluciones': 'Arquitecto de soluciones',
        'DBA': 'DBA',
        'Scrum_master': 'Scrum master',
        'Otro': 'Otro',
    }

    # Obtener el valor seleccionado para opciones de interés
    opcion_elegida = datos_formulario.get('opciones_interes')

    # Obtener la descripción correspondiente a la opción elegida
    interes_descripcion = opciones_interes.get(opcion_elegida, 'No especificado')

    # Construir el mensaje del correo electrónico
    subject = 'Nueva solicitud de posible trabajador'
    message = f'Nombre: {datos_formulario["nombre"]}\n' \
              f'Email: {datos_formulario["email"]}\n' \
              f'Profesión: {datos_formulario["profesion"]}\n' \
              f'Opciones de interés: {interes_descripcion}\n' \
              f'Link de LinkedIn: {datos_formulario["linkedin_url"]}\n' \
              f'CV Adjunto a continuación'

    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['informaticakyvm@gmail.com']

    email = EmailMessage(subject, message, email_from, recipient_list)

    # Adjuntar el archivo recibido al correo electrónico sin leerlo
    email.attach(archivo_adjunto.name, archivo_adjunto.file.read(), archivo_adjunto.content_type)

    # Envía el correo electrónico
    try:
        email.send()
    except Exception as e:
        print("Error al enviar el correo electrónico:", e)


def confirmacion_2(request):
    return render(request, 'Inicio/confirmacion_formulario_2.html')