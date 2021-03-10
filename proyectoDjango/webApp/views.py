from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from django.http import response

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def plantilla_padre(request):
    return render(request, 'padre.html')

def ejemplo_herencia(request):
    return render(request, 'hija1.html')    

def ejemplo_herencia_dos(request):
    return render(request, 'hija2.html')    