from django.shortcuts import render, redirect
from .forms import *
from .models import *


def ProductsAdd(request):

    context = {
        'product_form':Product_Form()
    }

    if request.method == 'POST':
        product_form = Product_Form(request.POST)
        if product_form.is_valid():
            product_form.save()


    return render(request,'products_add.html',context)

def AllProducts(request):
    context = {
        'all_products':Product.objects.all()
    }
    all_products = Product.objects.all()
    return render(request,'products.html',context)

def DeleteProduct(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/inventory/products/')

def UpdateProduct(request,id):
    product = Product.objects.get(id=id)

    context = {
        'product_form':Product_Form(instance=product)
    }
    if request.method == 'POST':
        product_form = Product_Form(request.POST,instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')

    return render(request,'products_add.html',context)
