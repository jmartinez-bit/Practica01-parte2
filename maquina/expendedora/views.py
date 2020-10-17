from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Productos

def index(request):
    productos = Productos.objects.order_by('id')
    context = {'productos':productos}
    return render(request, 'index.html', context)

def enviar(request):
    saldo = request.POST['saldo']
    codigo = request.POST['codigo']
    producto = opc(codigo)
    context = saldo_rest(saldo, producto.precio)
    return HttpResponse(context)

def saldo_rest(saldo, costo):
    saldo = float(saldo)
    costo = float(costo)
    
    if saldo < costo:
        msj = 'No tiene el monto para el producto seleccionado'
        return msj
    else:
        restante = saldo-costo
        msj = 'El saldo restante es: ' + str(restante) +'\nGracias por la compra !!!'
        return msj

def opc(opc):
    opc = int(opc)
    if opc>=1 and opc<=10:
        producto = Productos.objects.get(id=opc)
        return producto


    else:
        msj = 'La opcion ingresada es incorrecta'
        return msj
