from django.db import models
from django.db.models.signals import pre_save
# slugify - это функция берет имя и преображает в формат slug:
# >>>slugify(' Joel is a slug ')
# 'joel-is-a-slug'
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse   # функция для перехода по продуктам


class ProductManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset()


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)    # чтоб поле заполнения ссылки можно было оставлять свободным
    objects = ProductManager()

    def __str__(self):          #метод, чтоб правильно отображалось в админке название Протеины, а неProducts(object1)
        return self.name

    def get_absolute_url(self):             #переход по ссылке
        return reverse('product_detail', kwargs={'product_slug': self.slug})


def pre_save_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_product_slug, sender=Product)     #чтоб slug работал присоединяем его к Product


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ItemManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ItemManager, self).get_queryset().filter(available=True, new_item=True)


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    new_item = models.BooleanField(default=True)
    objects = ItemManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):             #переход по ссылке
        return reverse('item_detail', kwargs={'item_slug': self.slug})

    # def get_absolute_url(self):
    #     return reverse('people.views.details', args=[str(self.id)])   ex.


def pre_save_item_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug


pre_save.connect(pre_save_item_slug, sender=Item)
