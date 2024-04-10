from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),  # También mantén tu ruta existente para '/inicio/'
    path('contacto', views.contacto, name='contacto'),
    path('confirmacion', views.confirmacion, name='confirmacion'),
    path('form_personas', views.form_personas, name='form_personas'),
    path('confirmacion_2', views.confirmacion_2, name='confirmacion_2'),
    

]
