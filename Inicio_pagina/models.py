from django.db import models

class Formulario(models.Model):
    OPCIONES_CONTACTO = [
        ('telefono', 'Comunicarse por teléfono'),
        ('email', 'Comunicarse por email'),
    ]

    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100, blank=True, null=True, default=None)  # Cambios aquí
    telefono = models.IntegerField()
    email = models.CharField(max_length=150)
    motivo_contacto = models.CharField(max_length=400)
    forma_contacto = models.CharField(max_length=20, choices=OPCIONES_CONTACTO)

    def __str__(self):
        return self.empresa

class FormularioPersonas(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    profesion = models.CharField(max_length=80)
    cv = models.FileField(upload_to='cv/')  # Campo para adjuntar archivos
    linkedin_url = models.URLField(blank=True, null=True, default=None)  # Campo para la URL de LinkedIn

    def __str__(self):
        return self.nombre