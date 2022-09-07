from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

def index(request):
    return HttpResponse("Hola, mundo")

def newMembers(request):
    #print(request.method)
    if request.method == 'POST':
        return HttpResponse("Va a agregar un nuevo miembro")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getMembers(request):
    if request.method == 'GET':
        return HttpResponse("Esta es la información de los miembros")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")