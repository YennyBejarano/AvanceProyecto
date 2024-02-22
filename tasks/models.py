from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class task (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True , blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '- by ' + self.user.username
 

class Usuarios(models.Model):
    TIPOS_DE_USUARIO = (
        ('admin', 'Administrador'),
        ('normal', 'Usuario Normal'),
    )

    
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS_DE_USUARIO)
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Reunion(models.Model):
    reunion = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=255)
    fecha = models.DateTimeField(null=True,blank=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return str(self.reunion ) + '- by ' + self.asunto


class Asistencia(models.Model):
    fecha = models.DateTimeField(null=True,blank=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    asistio = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.fecha) + '- by ' + str(self.usuario)
    
    
    
class Anotacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField(null=True,blank=True)
    estado = models.CharField(max_length=255)
    respuesta = models.TextField(blank=True, null=True)
    
    
    




    



    
    

