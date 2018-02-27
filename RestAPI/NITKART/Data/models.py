from django.db import models


class DataModel(models.Model):
    image = models.ImageField()
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    seller_name = models.CharField(max_length=100, default=None)
    seller_phone_no = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.product_name
