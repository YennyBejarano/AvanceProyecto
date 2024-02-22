from django.forms import ModelForm
from .models import task
from django import forms
from .models import Usuarios,Asistencia,Reunion


class taskform(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'important', ]
        
        # tu_app/forms.py


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
        
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        


class ReunionForm(forms.ModelForm):
    class Meta:
        model = Reunion
        fields = ['asunto', 'fecha', 'descripcion']







