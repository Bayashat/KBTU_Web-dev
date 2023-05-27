from rest_framework import serializers

from api.models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # When creating new object, we don't need to provide id
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        print(validated_data)  # {'name': "Electronics"}
        category = Category.objects.create(name=validated_data.get('name', ''))  # or .create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('id', 'name', 'description')
        fields = "__all__"
        # read_only_fields = ('name', )
