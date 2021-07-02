from django.db import models
from .order import Order
from kokocorp.catalogue.models.product import Product

class Order_detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    cost = models.FloatField()

    def __str__(self):
        return f"{self.product} - {self.amount} - {self.cost}"