# coding:UTF-8 -*-
from django.db import models

# Create your models here.

class Product(models.Model):
    productname = models.CharField("product_name", max_length = 64)
    productdesc = models.CharField("product_desc", max_length = 200)
    producter = models.CharField("producter", max_length = 200)
    create_time = models.DateTimeField("create_time", auto_now = True)

    class Meta:
        verbose_name = "product_manage"
        verbose_name_plural = "product_manage"

    def __str__(self):
        return self.productname
