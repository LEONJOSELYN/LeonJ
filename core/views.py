from django.shortcuts import render

# Create your view

def holamundoCore(request):
    return render(request,'core.html')

def INICIO(request):
    return render(request,'core.html')

def Nuestrosproductos(request):
    return render(request,'Nuestros Productos.html')

def Quienessomos(request):
    return render(request,'Quienes somos.html')

def Contactos(request):
    return render(request,'Contactos.html')

def Bebidas(request):
    return render(request,'bebidas.html')

def Dulces(request):
    return render(request,'dulces.html')

def Verduras(request):
    return render(request,'verduras.html')

def Carnes(request):
    return render(request,'carnes.html')

def Higiene(request):
    return render(request,'higiene.html')

def Quejas(request):
    return render(request,'contactanos.html')

def Trabaja(request):
    return render(request,'trabaja.html')


#===========================HERENCIA======================================

def inicioh(request):
    return render(request,'herencia/inicioh.html')

def contactosh(request):
    return render (request,'herencia/contactosh.html')

def nuestrosproductosh(request):
    return render (request,'herencia/nuestrosproductosh.html')

def quienesomosh(request):
    return render (request,'herencia/quienesomosh.html')
