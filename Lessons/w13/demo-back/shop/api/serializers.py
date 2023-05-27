from rest_framework import serializers

from .models import Category, Product


class CategorySerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name', ''))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', '')
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 默认是这样的
    products = serializers.StringRelatedField(many=True, read_only=True)  # Will display the string representation of the related object.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ('id', 'name', 'user',  'products')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        # fields = ('id', 'name', 'description')
        fields = "__all__"
        # read_only_fields = ('name', )


#         Showed Nested objects
class Product2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description')


class CategorySerializer2(serializers.ModelSerializer):
    products = Product2Serializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ('id', 'name', 'user',  'products')
