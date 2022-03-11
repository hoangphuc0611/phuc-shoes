from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from products.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
# f = open('/data/shoes.json')
# data = json.load(f)
# print(data)
from products.models import Product
from .models import Cart, CartItems



def load_all(request):
    total=0.00
    products = Product.objects.all()
    cartitems = CartItems.objects.all()
    list_id =[]
    if len(cartitems) != 0:
        cart = Cart.objects.get(user=cartitems[0].user)
        total = cart.total_price
        list_item = cartitems
        list_id = [temp.product.id for temp in list_item]
    else:
        list_item=None
    
    context = {'object_list': products,
                'item_list': list_item,
                'total_price': total,
                'list_id': list_id}
    return render(request, 'home.html',context)

def create_cartitem(request,pk):
    product = Product.objects.get(id=pk)
    cart = Cart.objects.all()[0]
    user = cart.user
    cart_item = CartItems(cart=cart, user=user, product=product, quantity=1)
    cart_item.save()
    return redirect(load_all)

def subtract(request, id):
    product = Product.objects.get(id=id)
    cart_item = CartItems.objects.get(product=product)
    cart_item.quantity = cart_item.quantity - 1
    if cart_item.quantity == 0:
        cart_item.save()
        cart_item.delete()
    else:
        cart_item.save()
    return redirect(load_all)

def addition(request, id):
    product = Product.objects.get(id=id)
    cart_item = CartItems.objects.get(product=product)
    cart_item.quantity = cart_item.quantity + 1
    cart_item.save()
    return redirect(load_all)

def remove(request, id):
    product = Product.objects.get(id=id)
    cart_item = CartItems.objects.get(product=product)
    cart = Cart.objects.all()[0]
    cart.total_price -= round(cart_item.price,2)
    cart.total_price = round(cart.total_price,2)
    cart.save()
    cart_item.delete()
    return redirect(load_all)