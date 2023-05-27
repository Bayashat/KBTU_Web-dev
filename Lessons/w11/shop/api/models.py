from django.db import models

# Create your models here.
'''
Table relations

1) One to One   -   each "User" can have only one "Profile"
2) One to Many  -   each "Category" can have many "Products"
3) Many to Many -   each "Product" can have many "Tags" and each "Tag" can have many "Products"

'''


# class Tag(models.Model):
#     name = models.CharField(max_length=255)


# class ProductTag(models.Model):
#     product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='tags')
#     tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='products')


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products',
                                 null=True)  # models.SET_NULL / SET_DEFAULT / PROTECT

    # tags = models.ManyToManyField(Tag, related_name='products', blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-name"]  # default ordering for all queries
        # db_table = 'my_product'  # will create table 'my_product' instead of 'api_product'

    def to_json(self):  # Simple function to convert current object to json
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category.name
        }

    # To string method
    def __str__(self):
        return f"{self.name} - {self.price}"


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
