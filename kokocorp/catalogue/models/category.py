from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return f"{self.name}"