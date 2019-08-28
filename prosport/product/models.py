# from django.db import models
#
# # Create your models here.
#
#
# class ProductManager(models.Manager):
#
#     def all(self, *args, **kwargs):
#         return super(ProductManager, self).get_queryset()
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(blank=True)    # чтоб поле заполнения ссылки можно было оставлять свободным
#     objects = ProductManager()
#
#     def __str__(self):          #метод, чтоб правильно отображалось в админке название Протеины, а неProducts(object1)
#         return self.name
