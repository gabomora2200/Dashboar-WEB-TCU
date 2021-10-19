from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered_orders = orders.filter(status='Entregada').count()
    pending_orders = orders.filter(status='Pendiente').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered_orders': delivered_orders, 'pending_orders': pending_orders}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request):
    return render(request, 'accounts/customer.html')


'''
--accounts
----templates
------accounts
------- dasboard.html
------- dasboard.html
------- dasboard.html
'''
