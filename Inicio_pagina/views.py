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
            formulario.save()
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
    # Configuración del servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Configura tu dirección de correo y contraseña
    correo_emisor = "informaticakyvm@gmail.com"
    contraseña = "uhjq bjly zgzf blmo"

    # Dirección de correo destino
    correo_destino = "informaticakyvm@gmail.com"

    # Construir el mensaje
    mensaje = MIMEMultipart()
    mensaje["From"] = correo_emisor
    mensaje["To"] = correo_destino
    mensaje["Subject"] = "Nueva solicitud de posible trabajador"

    cuerpo_mensaje = f'Nombre: {datos_formulario["nombre"]}\n' \
                    f'Email: {datos_formulario["email"]}\n' \
                    f'Profesión: {datos_formulario["profesion"]}\n' \
                    f'Link de LinkedIn: {datos_formulario["linkedin_url"]}\n' \
                    f'CV Adjunto a continuación'

    mensaje.attach(MIMEText(cuerpo_mensaje, "plain"))

    if archivo_adjunto:
        adjunto = MIMEBase('application', 'octet-stream')
        adjunto.set_payload(archivo_adjunto.read())
        encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', 'attachment', filename=os.path.basename(archivo_adjunto.name))
        mensaje.attach(adjunto)

    # Iniciar conexión SMTP y enviar correo
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(correo_emisor, contraseña)
            server.sendmail(correo_emisor, correo_destino, mensaje.as_string())
        return True
    except Exception as e:
        print("Error al enviar el correo:", e)
        return False

def confirmacion_2(request):
    return render(request, 'Inicio/confirmacion_formulario_2.html')
