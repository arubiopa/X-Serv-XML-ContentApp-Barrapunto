from django.shortcuts import render
from models import Pages
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from xmlbarrapunto import getNews

barrapunto = ""
def update(request):
    global barrapunto
    barrapunto = getNews()
    return HttpResponse("Barrapunto actualizado" + barrapunto)

@csrf_exempt
def cms(request, recurso):
    if request.method == "GET":
        try:
    		contenido = Pages.objects.get(name=recurso)
    		return HttpResponse(contenido.name+ ':' + contenido.page + barrapunto)
    	except Pages.DoesNotExist:
    		return HttpResponseNotFound("Recurso no encontrado: " + recurso + barrapunto)

    if request.method == "PUT":
        pagina = Pages(name=recurso, page=request.body)
        pagina.save()
        return HttpResponse("Pagina guardada: "+ request.body + barrapunto)
