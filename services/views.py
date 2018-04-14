from django.shortcuts import render
# Importando la funcion HttpResponse, sino no se puede usar
from django.http import HttpResponse

# Funcion index
def index(request):
    # Print sirve para imprimir
    print("Soy un log de servidor.")
    print(" -- Entrando al index --")
    return HttpResponse("hola q hace.")