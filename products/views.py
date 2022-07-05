from django.http import HttpResponse
from django.shortcuts import render
from sympy import product
from .models import Product


def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})


def new(request):
   return HttpResponse("NEW  PRODUCTS")
