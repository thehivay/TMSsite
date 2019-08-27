from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('address/', views.address, name='address'),
    path('product/', views.product, name='product_detail'),
    path('item/', views.item, name='item_detail'),
]