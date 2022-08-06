from django.shortcuts import HttpResponse
from django.shortcuts import render
html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTESssss',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)

def reloj(request):
  data = {
    
      'titulo':'Reloj Biometrico',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  
  }
  return render(request, "reloj/reloj.html",data)
  

def ingresar(request):
  data = {
      'titulo':'Reloj Biometrico',
  }
  return render(request, "reloj/ingresar.html",data)

def index(request):
  data = {
      'titulo':'Registro',
      
  }
  return render(request, "reloj/index.html",data)
def calendario(request):
  data = {
      'titulo':'Calendario',
      
  }
  return render(request, "reloj/calendario.html",data)
def tarjeta(request):
  data = {
      'titulo':'Calendario',
      
  }
  return render(request, "reloj/tarjeta.html",data)