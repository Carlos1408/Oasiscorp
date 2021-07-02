from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"