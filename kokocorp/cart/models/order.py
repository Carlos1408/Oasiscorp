from django.db import models
from kokocorp.user.models.user import User

class Order(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.user} - {self.cost}"