from cmath import cos
import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Contacto.models import Contactos
from inventario.models import Productos
from shop.views import shoop
import smtplib
from email.message import EmailMessage
messageCliente='hola recibiste este correo ya que compraste un producto en licotapetusa: '
messageAdmin='Admin una compra fué realizada por: '
subject="Compra en Lico tapetusa"
message="subject : {}\n\n{}".format(subject,messageCliente)
messageAdmin="subject : {}\n\n{}".format(subject,messageAdmin)

# Create your views here.


def Datos_Entrega(request, pk):
    producto = Productos.objects.get(id=pk)
    return render (request, "plantilla.html", {{"producto":producto}})
    

def Enviar_datos(request):
    if request.method=="POST":

        nombre_apellido = request.POST["nombres"]
        id = request.POST["id"]
        correo = request.POST["correo"]
        Direccion = request.POST["Direccion"]
        departamento = request.POST["Depa"]
        ciudad = request.POST["ciudad"]
        telefono = request.POST["telefono"]
        costo = request.POST["costo"]
        nombre_pro = request.POST["nombre_producto"]
        data = Contactos(name=nombre_apellido, id=id, email= correo, adress=Direccion, local=departamento, city=ciudad, cellphone=telefono, cost=costo, product_name=nombre_pro )
        data.save()
        correoAdmin = 'pepetoo123321@gmail.com'
        server1=smtplib.SMTP('smtp.gmail.com','587')
        server1.starttls()
        server1.login('pepetoo123321@gmail.com','pepeto123456')
        server1.sendmail('pepetoo123321@gmail.com',correo,messageCliente,nombre_pro, costo)  
        server1.sendmail('pepetoo123321@gmail.com',correoAdmin,messageAdmin,nombre_pro, costo)                        
        print("se envio el correo ")

        return redirect('/shop/')
    
    else:

        return render (request, "plantilla.html")

