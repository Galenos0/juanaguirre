from django.shortcuts import render, redirect
from .forms import Postproducto
from .models import Producto


def add_product(request):

    if request.method== "POST":
        form = Postproducto(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect("/productos/")
        
    else:
        form= Postproducto()
        return render(request,
                "productos_add.html", 
                {"form":form})
    


def show_product(request):
    productos=Producto.objects.filter(estatus=True)

    if len(productos)==0:
        return redirect("/productos/agregar/")
    return render(request,
                    "productos_show.html",
                    {"data":productos})

