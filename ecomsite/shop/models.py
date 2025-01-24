from django.db import models



class Products(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=400)


class Order(models.Model):
    def __str__(self):
        return self.name

    items = models.CharField(max_length=2000)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zip = models.CharField(max_length=200)
    total = models.CharField(max_length=200, default=0)

