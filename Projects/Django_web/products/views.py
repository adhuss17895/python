from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})
#request: HTTP request


def new_page(request):
    return HttpResponse('Hello You can find new products here!!')
