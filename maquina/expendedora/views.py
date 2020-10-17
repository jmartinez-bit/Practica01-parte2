from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Productos

def index(request):
    productos = Productos.objects.order_by('id')
    context = {'productos':productos}
    return render(request, 'index.html', context)

def saldo_rest(saldo, costo):
    if saldo < costo:
        msj = 'No tiene el monto para el producto seleccionado'
        return msj
    else:
        restante = saldo-costo
        msj = 'El saldo restante es: ' + str(restante) +'\nGracias por la compra !!!'
        return msj


def opc(opc):
    if opc>=1 and opc<=10:
        i = 1
        while i <=10:
            if int(opc) == i:
                producto = Productos.objects.get(id=i)
                return producto

    else:
        msj = 'La opcion ingresada es incorrecta'
        return msj

'''
def productos():
    lista = []
    i = 1
    while i <=10:
        producto = Productos.objects.get(id=i)
        lista.append(producto)
        i += 1
    print(lista[0].precio)
'''