from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventario.models import Productos

# Create your views here.
def shoop(request):
    producto=Productos.objects.all()
    return render (request, 'tinda_licores.html',{"producto": producto})