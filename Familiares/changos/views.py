from django.shortcuts import render
from changos.models import Changos

# Create your views here.

def changos(request):
    todos = Changos.objects.all()
    context = {'todos' : todos}
    return render(request, 'changos.html', context = context )