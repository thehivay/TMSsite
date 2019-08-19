# Create your models here.

from django.db import models


class Products(models.Model):
    name = models.CharField
    slug = models.SlugField

