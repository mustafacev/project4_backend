from django.db import models
import time
# Create your models here.

class House (models.Model):

    title = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    address = models.TextField(max_length=200)
    realtor = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode= models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    bedrooms = models.CharField(max_length=100)
    bathroom = models.CharField(max_length=100)
    sqft = models.CharField(max_length=100)
    favorite_house = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']