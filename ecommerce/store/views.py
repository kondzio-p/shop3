from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items, 'order' : order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productID']
    action = data['action']

    print("Produkt: ", productId)
    print("Akcja: ", action)
    return JsonResponse('Item added', safe=False)
