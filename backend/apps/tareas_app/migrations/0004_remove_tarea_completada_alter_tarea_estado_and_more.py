# Generated by Django 5.1.4 on 2025-02-19 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableros_app', '0002_tablero_color_tablero_icono'),
        ('tareas_app', '0003_tarea_tablero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='completada',
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_progreso', 'En Progreso'), ('completada', 'Completada')], default='pendiente', max_length=15),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='tablero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='tableros_app.tablero'),
            preserve_default=False,
        ),
    ]
