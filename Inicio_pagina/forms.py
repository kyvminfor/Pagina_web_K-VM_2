from django import forms
from .models import Formulario
from .models import FormularioPersonas

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'nombre',
            'empresa',
            'telefono',
            'email',
            'motivo_contacto',
            'forma_contacto' 
        ]
        labels = {
            'nombre': 'Nombre completo',
            'empresa': 'Nombre empresa',
            'telefono': 'Telefono',
            'email': 'Correo electronico',
            'motivo_contacto': 'Motivo de contacto',
            'forma_contacto': 'Forma de contacto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'forma_contacto': forms.Select(attrs={'class': 'form-control'}),
        }
             
class FormularioPersonasForm(forms.ModelForm):
    class Meta:
        model = FormularioPersonas
        fields = [
            'nombre',
            'email',
            'profesion',
            'opciones_interes',
            'cv',
            'linkedin_url',
        ]
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
            'profesion': 'Profesión',
            'opciones_interes' : 'Opciones de interes',
            'cv': 'Curriculum Vitae',
            'linkedin_url': 'URL de LinkedIn',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'opciones_interes': forms.TextInput(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control-file'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
        }