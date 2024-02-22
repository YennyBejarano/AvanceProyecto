from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import task
from .forms import taskform
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import re
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import os
from .models import Asistencia , Anotacion , Reunion
from django.shortcuts import render, get_object_or_404
from .models import Usuarios
from .forms import UsuarioForm
from .forms import AsistenciaForm
from .forms import ReunionForm




def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        password = request.POST['password1']
        if (
            password == request.POST['password2']
            and len(password) >= 10
            and re.search(r'[A-Z]', password)  # al menos una mayúscula
            and re.search(r'[a-z]', password)  # al menos una minúscula
            and re.search(r'[\W_@+*]', password)  # al menos un carácter especial
        ):
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=password,email=request.POST['email'])
                user.save()
                login(request, user) 
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'el usuario ya existe'})

        return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'la longitud de las contraseñas no son requeridas o no coinciden o no cumplen los requisitos'})
   
 
   
    
 
def email():
    
    load_dotenv()
    email_sender = "yennybejarano937@gmail.com"
    password =  os.getenv("PASSWORD")
    email_reciver = "bejaranopatricia11@gmail.com"

    subject = "recuperar contraseña"
    body = f""" Inicio Exitoso.  {email_reciver}"""

    em = EmailMessage()
    em ["From"] = email_sender
    em ["To"] = email_reciver
    em ["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context() 

    with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context  ) as smtp:
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender,email_reciver,em.as_string())  
    return 
     
     
     
def recuperar(request):
    if request.method=='GET':
    
        return render(request,'recuperar.html')
    else:
         
        usuario=User.objects.get(email=request.POST['correo']) 
        print(usuario.password) 
        return render(request,'recuperar.html',{
            'user':usuario.email
        }) 
     
     
     
       
    

@login_required
def tasks(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})



@login_required
def tasks_completed(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})





@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": taskform})
    else:
        try:
            form = taskform(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": taskform, "error": "Error creating task."})





@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        Task = get_object_or_404(task, pk=task_id, user=request.user)
        Form = taskform(instance=Task)
        return render(request, 'task_detail.html', {"task": Task, "form": Form})
    else:
        try:
            Task = get_object_or_404(task, pk=task_id, user=request.user)
            form = taskform(request.POST, instance=Task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': Task, 'form': form, 'error': 'Error actualizando task.'})
    
    
    
  
  
  
@login_required  
def complete_task(request, task_id):
    Task = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST':
        Task.datecompleted = timezone.now()
        Task.save()
        return redirect('tasks')





@login_required
def delete_task(request, task_id):
    Task = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST':
        Task.delete()
        return redirect('tasks')    
    
    
  
    
    
@login_required
def desconectar(request):
    logout(request)
    return redirect('home')


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            
            return render(request, 'iniciarSesion.html', {'form': AuthenticationForm, 'error': 'el usuario o la contraseña  es incorrecto'})
        else:
            login(request, user)
            email()
            return redirect(tasks)








def agregar_usuario(request):
    
    if request.method == 'GET':
        
        form = UsuarioForm
        return render(request, 'agregar_usuario.html', {'form': form})
    else:

        try:
            form = Usuarios(tipo_usuario=request.POST['tipoUsuario'],cedula=request.POST['cedula'],nombre=request.POST['nombre']
                            ,direccion=request.POST['direccion'],celular=request.POST['celular'],email=request.POST['email'])
            form.save()
            return redirect('lista_usuarios')
        except IntegrityError:
            error="Datos existen"
            return render(request,'agregar_usuario.html',{'error':error})
    


def lista_usuarios(request):
        usuarios=Usuarios.objects.all()
        return render(request,'lista_usuarios.html',{'usuarios':usuarios})
    
    
    
    
    
def editar(request,usuario_id):
    if request.method == 'GET':
        usuario = get_object_or_404(Usuarios, pk=usuario_id)
        Form = UsuarioForm(instance=usuario)
        return render(request, 'editar.html', {'usuario': usuario, 'form': Form})
    else:
        try:
            usuario = get_object_or_404(Usuarios,pk=usuario_id)
            form = UsuarioForm(request.POST, instance=usuario)
            form.save()
            return redirect('lista_usuarios')
        except ValueError:
            return render(request, 'editar.html', {'usuario': usuario, 'form': form, 'error': 'Error actualizando task.'})
        
        
def borrar(request, usuario_id):
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    if request.method == 'GET':
        usuario.delete()
        return redirect('lista_usuarios')
        

def busqueda(request):
    if request.method=='GET':
        usuario = Usuarios.objects.all()
        return render(request,'lista_usuarios.html',{'usuarios':usuario})
    else:
        usuario = Usuarios.objects.filter(cedula__icontains=request.POST['nombre'])
        return render(request,'lista_usuarios.html',{'usuarios':usuario})
    
    
    


def asistencia_lista(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'asistencia_lista.html', {'asistencias': asistencias})



def lista_anotaciones(request):
    anotaciones = Anotacion.objects.all()
    return render(request, 'lista_anotaciones.html', {'anotaciones': anotaciones})

def lista_reuniones(request):
    reuniones = Reunion.objects.all()
    return render(request, 'lista_reuniones.html', {'reuniones': reuniones})






def editar_asistencia(request,usuario_id):
    if request.method == 'GET':
        usuario = get_object_or_404(Asistencia,pk=usuario_id)
        Form = AsistenciaForm(instance=usuario)
        return render(request, 'editar_asistencia.html', {'usuario': usuario, 'form': Form})
    else:
        try:
            usuario = get_object_or_404(Asistencia,pk=usuario_id)
            form = AsistenciaForm(request.POST, instance=usuario)
            form.save()
            return redirect('asistencia_lista')
        except ValueError:
            return render(request, 'editar_asistencia.html', {'usuario': usuario, 'form': form, 'error': 'Error actualizando task.'})
        
        
        
def reunion_asistencia(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})



def reunion_asistencia(request, reunion_id):
    reuniones = Reunion.objects.filter(reunion=reunion_id)
    return render(request, 'reunion_asistencia.html', {'reuniones': reuniones})






def agregar_reunion(request):
    if request.method == 'POST':
        form = ReunionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reuniones')  # Redirigir a la página de lista de reuniones
    else:
        form = ReunionForm()

    return render(request, 'agregar_reunion.html', {'form': form})

