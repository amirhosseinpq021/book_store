from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
