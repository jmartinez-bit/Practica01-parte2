from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Productos

def index(request):
    productos = Productos.objects.order_by('id')
    context = {'productos':productos}
    return render(request, 'index.html', context)
