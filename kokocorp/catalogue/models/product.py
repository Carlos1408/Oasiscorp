from django.db import models
from .product import Product
from .supplier import Supplier

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    image = models.ImageField()
    features = models.JSONField()

    def __str__(self):
        return f"{self.name}"