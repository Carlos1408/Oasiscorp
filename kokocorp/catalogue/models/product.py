from django.db import models
from .category import Category
from .supplier import Supplier

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank = True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='product')
    features = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name}"
