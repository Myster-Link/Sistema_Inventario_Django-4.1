from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


@login_required
def inventario(request):

    categorias = CategoriasProducto.objects.all()
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        nombre_producto = request.POST['nombre_producto']
        codigo_producto = request.POST['codigo_producto']
        categoria_producto = request.POST['categoria_producto']
        proveedor_producto = request.POST['proveedor_producto']
        stock_producto = request.POST['stock_producto']
        precio_producto = request.POST['precio_producto']
        descripcion_producto = request.POST['descripcion_producto']
        imagen_producto = request.FILES['imagen_producto']

        # Estas vaiables son instancias de los modelos convierten los datos post en una instancia para haci guardarlos
        obj_categoria = CategoriasProducto.objects.get(id=categoria_producto)
        obj_proveedor = Proveedor.objects.get(id=proveedor_producto)

        producto = Producto(nombre=nombre_producto,
                            codigo_producto=codigo_producto,
                            categoria=obj_categoria,
                            proveedor=obj_proveedor,
                            stock=stock_producto,
                            precio=precio_producto,
                            descripcion=descripcion_producto,
                            imagen=imagen_producto)

        producto.save()

        return redirect('/inventario/')

    return render(request, 'Inventario/inventario.html', {'productos': productos, 'categorias': categorias, 'proveedores': proveedores})


@login_required
def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('inventario')


@login_required
def editar(request, id):

    categorias = CategoriasProducto.objects.all()
    proveedores = Proveedor.objects.all()
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        nombre_producto = request.POST['nombre_producto']
        codigo_producto = request.POST['codigo_producto']
        categoria_producto = request.POST['categoria_producto']
        proveedor_producto = request.POST['proveedor_producto']
        stock_producto = request.POST['stock_producto']
        precio_producto = request.POST['precio_producto']
        descripcion_producto = request.POST['descripcion_producto']
        imagen_producto = request.FILES['imagen_producto'] 

        # Estas vaiables son instancias de los modelos convierten los datos post en una instancia para haci guardarlos
        obj_categoria = CategoriasProducto.objects.get(id=categoria_producto)
        obj_proveedor = Proveedor.objects.get(id=proveedor_producto)

        producto = Producto(nombre=nombre_producto,
                            codigo_producto=codigo_producto,
                            categoria=obj_categoria,
                            proveedor=obj_proveedor,
                            stock=stock_producto,
                            precio=precio_producto,
                            descripcion=descripcion_producto,
                            imagen=imagen_producto)
        producto.save()

        return redirect('/inventario/')

    return render(request, 'Inventario/editar.html', {'producto': producto, 'categorias': categorias, 'proveedores': proveedores})


@login_required
def add_categoria(request):

    if request.method == 'POST':
        nombre_categoria = request.POST['nombre_categoria']

        categoria = CategoriasProducto(nombre=nombre_categoria)
        categoria.save()

    return redirect('/inventario/')


@login_required
def add_proveedor(request):

    if request.method == 'POST':
        nombre_proveedor = request.POST['nombre_proveedor']

        proveedor = Proveedor(nombre=nombre_proveedor)
        proveedor.save()

    return redirect('/inventario/')
