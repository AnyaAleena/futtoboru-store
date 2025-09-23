import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sportswear', 'Sportswear'),
        ('footwear', 'Footwear'),
        ('accessories', 'Accessories'),
        ('others', 'Others'),
    ]

    COLOR_CHOICES = [
        ('black', 'Black'),
        ('white', 'White'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('gold', 'Gold'),
        ('purple', 'Purple'),
        ('pink', 'Pink')
    ]

    SIZE_CHOICES = [
        ("s", "S/38"),
        ("m", "M/39"),
        ("l", "L/40"),
        ("xl", "XL/41"),
        ("xxl", "XXL/42"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField(null=True)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='others')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='white')
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    

    def __str__(self):
        return self.name