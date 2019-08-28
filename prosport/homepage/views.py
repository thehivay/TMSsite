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
    context = {'products': products}
    return render(request, 'homepage/address.html', context)


def item_view(request, item_slug):
    products = Product.objects.all()
    item = Item.objects.get(slug=item_slug)
    context = {'item': item, 'products': products}
    return render(request, 'homepage/item.html', context)


def product_view(request, product_slug):
    products = Product.objects.all()      #!иначе не будет отображать колонка с продуктами
    product = Product.objects.get(slug=product_slug)
    items_of_product = Item.objects.filter(product=product)
    context = {'product': product,
               'products': products,
               'items_of_product': items_of_product,
               }
    return render(request, 'homepage/product.html', context)

