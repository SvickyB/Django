from django.shortcuts import render, redirect
from .forms import *
from .models import *


def CustomersAdd(request):

    context = {
        'customer_form':Customer_Form()
    }

    if request.method == 'POST':
        customer_form = Customer_Form(request.POST)
        if customer_form.is_valid():
            customer_form.save()


    return render(request,'customers_add.html',context)

def AllCustomers(request):
    context = {
        'all_customers':Customer.objects.all()
    }
    all_products = Customer.objects.all()
    return render(request,'customers.html',context)

def DeleteCustomers(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/order/customers/')

def UpdateCustomers(request,id):
    customer = Customer.objects.get(id=id)

    context = {
        'customer_form':Customer_Form(instance=customer)
    }
    if request.method == 'POST':
        customer_form = Customer_Form(request.POST,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/order/customers/')

    return render(request,'customers_add.html',context)

def OrdersAdd(request):

    context = {
        'orders_form':Orders_Form()
    }

    if request.method == 'POST':
        selected_product=Product.objects.get(id=request.POST['product_reference'])
        amount=float(selected_product.price)*float(request.POST['quantity'])
        gst_amount=(amount*selected_product.gst)/100

        bill_amount=amount+gst_amount

        new_order=Orders(Customer_reference_id=request.POST['Customer_reference'],
        product_reference_id=request.POST['product_reference'],
        order_number=request.POST['order_number'],
        order_date=request.POST['order_date'],
        quantity=request.POST['quantity'],
        amount=amount,
        gst_amount=gst_amount,
        bill_amount=bill_amount)

        new_order.save()

        return redirect('/order/orders/')

    return render(request,'orders_add.html',context)   

def OrdersList(request):
    context = {
        'all_orders':Orders.objects.all()
    }
    return render(request,'orders.html',context)

def OrdersDelete(request,id):
    order = Orders.objects.get(id=id)
    order.delete()
    return redirect('/order/orders/')

def OrdersUpdate(request,id):
    order = Orders.objects.get(id=id)

    context = {
        'orders_form':Orders_Form(instance=order)
    }
    if request.method == 'POST':
        selected_product=Product.objects.get(id=request.POST['product_reference'])
        amount=float(selected_product.price)*float(request.POST['quantity'])
        gst_amount=(amount*selected_product.gst)/100
        bill_amount=amount+gst_amount

        order_filter=Orders.objects.filter(id=id)
        order_filter.update(Customer_reference_id=request.POST['Customer_reference'],
        product_reference_id=request.POST['product_reference'],
        order_number=request.POST['order_number'],
        order_date=request.POST['order_date'],
        quantity=request.POST['quantity'],
        amount=amount,
        gst_amount=gst_amount,
        bill_amount=bill_amount)

        return redirect('/order/orders/')

    return render(request,'orders_add.html',context)