"""
URL configuration for djangoLogin project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.contrib.auth import views as auth_views
from tasks.views import agregar_usuario,  lista_usuarios , asistencia_lista , lista_reuniones, lista_anotaciones, editar_asistencia,reunion_asistencia, agregar_reunion
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete/',
         views.complete_task, name='complete_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('logout/', views.desconectar, name='logout'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/reset_password.html"),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complet.html"),
         name='password_reset_complete'),

    path('agregar_usuario/', agregar_usuario, name='agregar_usuario'),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('editar/<int:usuario_id>/', views.editar, name='editar'),
    path('borrar/<int:usuario_id>/', views.borrar, name='borrar'),
    path('busqueda/', views.busqueda, name='busqueda'),

    path('asistencia/', asistencia_lista, name='asistencia_lista'),
    path('anotaciones/', lista_anotaciones, name='lista_anotaciones'),
    path('reuniones/', lista_reuniones, name='lista_reuniones'),
    path('editar_asistencia/<int:usuario_id>/', editar_asistencia, name='editar_asistencia'),
    path('reunion_asistencia/<int:reunion_id>/', reunion_asistencia, name='reunion_asistencia'),
    
    path('agregar_Reunion/', agregar_reunion, name='agregar_reunion'),
    


    
    

]

