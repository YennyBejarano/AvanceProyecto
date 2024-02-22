from django.contrib import admin
from .models import task,Reunion,Anotacion,Asistencia,Usuarios


class taskadmin(admin.ModelAdmin):
    readonly_fields =("created", )


# Register your models here.
admin.site.register(task, taskadmin)
admin.site.register(Reunion)
admin.site.register(Asistencia)
admin.site.register(Anotacion)
admin.site.register(Usuarios)

