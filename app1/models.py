from django.db import models


# default model manager --> objects


# custom_model_manager
class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(in_stock=True)


class InStockBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(in_stock=True)


class OnSaleBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(on_sale=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    in_stock = models.BooleanField()
    on_sale = models.BooleanField(default=True)
    objects = BookManager()
    in_stock_books = InStockBookManager()
    on_sale_books = OnSaleBookManager()

    def __str__(self):
        return f'{self.title}   {self.in_stock}  {self.on_sale}'
