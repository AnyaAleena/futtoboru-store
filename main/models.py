from django.db import models

class Product(models.Model):
        
    name = models.CharField(max_length=30)
    price = models.IntegerField
    description = models.TextField
    thumbnail = models.URLField
    category = models.CharField
    is_featured = models.BooleanField
    stock = models.IntegerField
    rating = models.IntegerField
    color = models.TextField
    size = models.CharField(max_length=3)
    

    
    def __str__(self):
        return self.title