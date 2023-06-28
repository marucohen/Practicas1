from django.contrib import admin

# Register your models here.
from .models import Profesor, Estudiante, Curso, Entregable

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Entregable)