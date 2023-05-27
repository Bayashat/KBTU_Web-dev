from django.db import models

# Create your models here.
'''
create table product(
    id INTEGER,
    name VARCHAR(255,
    ...
);
'''

# ORM - Object Relational Mapping


class Product(models.Model):  # 继承 models.Model 使得 Product 类成为一个数据库模型. 默认情况下，Django 会自动为每个模型添加一个主键字段 id (自增长的整数类型)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

    # To String method 
    
    def __str__(self):
        return f"{self.name} - {self.price}"

