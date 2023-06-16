from django.http import HttpResponse
from django.template import loader
from AppPractica.models import Curso

def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context

# def probando_template(request):

#     nombre = "Maru"
#     apellido = "Cohen"
#     diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4, 8, 9, 10, 7, 8]}

#     # Abrimos el archivo html
#     mi_html = open('C:\\Users\\Windows11\\Desktop\\Maru\\Cursos\\Curso Python\\2023\\Prácticas con DJANGO\\Practicas1\\Practica_1\\Practica_1\\plantillas\\index.html')

#     # Creamos el template haciendo uso de la clase Template
#     plantilla = Template(mi_html.read())

#     # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
#     mi_html.close()

#     # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
#     mi_contexto = Context(diccionario)

#     # Terminamos de construír el template renderizándolo con su contexto
#     documento = plantilla.render(mi_contexto)

#     return HttpResponse(documento)

def usando_loader(request):
    nombre = "Maru"
    apellido = "Cohen"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def curso(request, nombre, numero):
    curso = Curso(nombre=nombre, camada=int(numero))
    curso.save()
    documento = f"Curso: {curso.nombre}<br>Camada: {curso.camada}"
    
    return HttpResponse(documento)