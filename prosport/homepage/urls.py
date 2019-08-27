from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('address/', views.address, name='address'),
    path('product/(<product_slug>)', views.product, name='product_detail'),
    path('item/(<item_slug>)', views.item, name='item_detail'),


]

