import json
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

from .models import Members

def index(request):
    return HttpResponse("Hola, mundo")

def newMembers(request):
    #print(request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #print(data)
            #print(type(data))
            member = Members(
                name = data["nombre"],
                email = data["correo"]
            )
            #print(member)
            member.save()
            return HttpResponse("Nuevo miembro agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getMembers(request):
    if request.method == 'GET':
        members = Members.objects.all()
        allMembersData = []
        for x in members:
            data = {"documento": x.id, "nombre": x.name, "email": x.email}
            allMembersData.append(data)
        dataJson = json.dumps(allMembersData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")