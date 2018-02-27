from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField()  # Opening stock
    close = models.FloatField()  # closing stock
    volume = models.IntegerField()  # No. of people

    def __str__(self):
        return self.ticker
