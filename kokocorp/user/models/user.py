from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birth_date = models.DateField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.email}"