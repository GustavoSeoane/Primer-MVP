from django.http import HttpResponse
from django.shortcuts import render


def entrega (request):
    return HttpResponse ("<h1>Hola Gustavo, te entrego el entregable solicitado<h1>")

def despedida (request):
    return HttpResponse ("<h2>Hasta Luego, nos vemos en la clase =)<h2>")

def probando_template (request):
    context = {
        'Nombre' : 'Gustavo',
        'Apellido' : 'Seoane'
    }
    return render(request, 'template1.html', context = context)
