from django.shortcuts import render

def inicio(request):
    return render(request, "AppPractica/index.html")

def cursos(request):
    return render(request, "AppPractica/cursos.html")

def profesores(request):
    return render(request, "AppPractica/profesores.html")

def estudiantes(request):
    return render(request, "AppPractica/estudiantes.html")

def entregables(request):
    return render(request, "AppPractica/entregables.html")