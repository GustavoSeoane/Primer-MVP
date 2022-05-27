from django.http import HttpResponse
from django.shortcuts import render


def entrega (request):
    return HttpResponse ("<h1>Hola Gustavo, te entrego el entregable solicitado<h1>")

def index (request):
    return render(request, 'index.html')

def probando_template (request):
    context = {
        'Nombre' : 'Gustavo',
        'Apellido' : 'Seoane'
    }
    return render(request, 'template1.html', context = context)
