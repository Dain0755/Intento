from cmath import cos
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Contacto.models import Contactos
from inventario.models import Productos
from tienda.views import shoop


# Create your views here.


def Datos_Entrega(request, pk):
    producto = Productos.objects.get(id=pk)
    return render (request, "plantilla.html", {"producto":producto})
    

def Enviar_datos(request):
    if request.method=="POST":

        nombre_apellido = request.POST["nombres"]
        id = request.POST["id"]
        correo = request.POST["correo"]
        Direccion = request.POST["direccion"]
        departamento = request.POST["Depa"]
        ciudad = request.POST["ciudad"]
        telefono = request.POST["telefono"]
        costo = request.POST["costo"]
        nombre_pro = request.POST["nombre_producto"]
        data = Contactos(nombre_apellido=nombre_apellido, id=id, correo= correo, direccion=Direccion, departamento=departamento, ciudad=ciudad, celular=telefono, pagar=costo, producto_Comprado=nombre_pro )
        data.save()

        if request.method=="POST":
            Productos.cantidad_stock =int(Productos.cantidad_stock)-int(request.POST["stock"])
            Productos.save() 
        
        return redirect('/shop/')
    
    else:

        return render (request, "plantilla.html")

