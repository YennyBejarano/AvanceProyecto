# Generated by Django 5.0.1 on 2024-02-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_reunion_usuarios_alter_task_datecompleted_anotacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='asistio',
            field=models.BooleanField(default=False),
        ),
    ]
