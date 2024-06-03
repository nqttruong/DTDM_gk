from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Coffee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    image = models.CharField(max_length=10000)

    def __str__(self):
        return self.name

class Order(models.Model):
    stt = models.AutoField(primary_key=True)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, default=1)  # Sử dụng giá trị mặc định là 1
    quantity = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return f"Order {self.stt}"

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.coffee.price
        super().save(*args, **kwargs)