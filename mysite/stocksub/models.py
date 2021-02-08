from django.db import models

class Subscription(models.Model):
    ticker = models.CharField('Stock Ticker', max_length=10)
    number = models.CharField('Phone Number (Add contry code, e.g. +1216748938)', max_length=12)
    date_sub = models.DateTimeField('date_sub', auto_now_add=True)

    class Meta:
        unique_together = ['ticker', 'number']