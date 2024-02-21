from django.db import models

class Formulario(models.Model):
    OPCIONES_CONTACTO = [
        ('telefono', 'Comunicarse por teléfono'),
        ('email', 'Comunicarse por email'),
    ]

    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100, blank=True, null=True, default=None)
    telefono = models.IntegerField()
    email = models.CharField(max_length=150)
    motivo_contacto = models.CharField(max_length=400)
    forma_contacto = models.CharField(max_length=20, choices=OPCIONES_CONTACTO)

    def __str__(self):
        return self.empresa

class FormularioPersonas(models.Model):
    OPCIONES_INTERES = [
        ('Programacion', 'Programación'),
        ('Gestion de Proyectos', 'Gestión de Proyectos'),
        ('Soporte técnico', 'Soporte técnico'),
        ('Testing', 'Testing'),
        ('Arquitecto de soluciones', 'Arquitecto de soluciones'),
        ('DBA', 'DBA'),
        ('Scrum master', 'Scrum master'),
        ('Marketing digital','Marketing digital'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    profesion = models.CharField(max_length=80)
    opciones_interes = models.CharField(max_length=400, choices=OPCIONES_INTERES)
    cv = models.FileField(upload_to='cv/')
    linkedin_url = models.URLField(blank=True, null=True, default=None)

    def __str__(self):
        return self.nombre
