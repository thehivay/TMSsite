from django.shortcuts import render
from homepage.models import Product
from homepage.models import Item

# Create your views here. Здесь происходит вся бизнес логика, в которой делается выборка из базы данных,
#                         чтоб подготовить вывод ее в шаблоне .html


def index(request):
    products = Product.objects.all()
    items = Item.objects.all()
    context = {'products': products, 'items': items}
    return render(request, 'homepage/home.html', context)


def address(request):
    products = Product.objects.all()
    items = Item.objects.all()
    context = {'products': products, 'items': items}
    return render(request, 'homepage/home.html', context)



