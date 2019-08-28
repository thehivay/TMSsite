# from django.db import models
# from django.urls import reverse
#
# # Create your models here.
#
#
# class ItemManager(models.Manager):
#
#     def all(self, *args, **kwargs):
#         return super(ItemManager, self).get_queryset().filter(available=True, new_item=True)
#
#
# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     slug = models.SlugField(blank=True)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
#     description = models.TextField()
#     image = models.ImageField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     available = models.BooleanField(default=True)
#     new_item = models.BooleanField(default=True)
#     objects = ItemManager()
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):             #переход по ссылке
#         return reverse('item_detail', kwargs={'item.slug': self.slug})