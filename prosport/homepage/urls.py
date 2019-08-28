from django.urls import path
from . import views
from homepage.views import item_view, product_view


urlpatterns = [
    path('', views.index, name='index'),
    path('address/', views.address, name='address'),
    path('item/<item_slug>/', item_view, name='item_detail'),
    path('product/<product_slug>/', product_view, name='product_detail'),

]

