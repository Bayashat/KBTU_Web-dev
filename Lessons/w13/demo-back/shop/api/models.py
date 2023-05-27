from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} - {self.price}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
