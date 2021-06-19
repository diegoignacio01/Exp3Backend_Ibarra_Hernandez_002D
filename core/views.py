from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
# Create your views here.
def home(request):
    productos= Producto.objects.all() #aqui entrega todos los objetos de la clase vehiculo


    return render(request,'index.html',context={'datos':productos},)

def form_producto(request):
    if request.method=='POST':
        producto_form=productoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('home')
    else:
        producto_form=ProductoForm()
    return render(request,'core/form_crearproducto.html',{'producto_form':producto_form})

    