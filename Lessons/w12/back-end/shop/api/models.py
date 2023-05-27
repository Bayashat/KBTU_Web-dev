from django.db import models

# Create your models here.
'''
Table relations

1) One to One   -   each "User" can have only one "Profile"
2) One to Many  -   each "Category" can have many "Products"
3) Many to Many -   each "Post" can have many "Tags" and each "Tag" can have many "Posts"
'''



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} - {self.price}"

    def to_json(self):  # Simple function to convert current object to json
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category.name
        }


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    


"""         
# 1) without related_name
c = Category.objects.get(pk=1)
c.product_set.all()     # all products of category c

# 2) with related_name
c = Category.objects.get(pk=1)
c.products.all()        # all products of category c

"""