from django.urls import path
from AppPractica import views

urlpatterns = [
    path('', views.inicio),
    path('cursos/', views.cursos, name= "Cursos"),
    path('profesores/', views.profesores, name= "Profesores"),
    path('estudiantes/', views.estudiantes, name= "Estudiantes"),
    path('entregables/', views.entregables, name= "Entregables")
]