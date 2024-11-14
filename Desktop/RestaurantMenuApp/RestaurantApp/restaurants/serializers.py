from rest_framework import serializers
from .models import Restaurant, MainCategory, MenuCategory, Dish, Ingredient

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        
        
        
class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id', 'name']
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        
        
class DishNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name']
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        

        
class MenuCategorySerializer(serializers.ModelSerializer): 
    parent_name = serializers.StringRelatedField()
    dishes = DishNameSerializer(many = True, read_only = True)
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'image', 'parent', 'dishes']
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        
    
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        
        
        
class DishDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many = True, read_only = True)
    
    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'image', ]
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        
        
class MenuCategoryDetailSerializer(serializers.ModelSerializer):
    dishes = DishDetailSerializer(many = True, read_only = True)
    
    class Meta:
        model = MenuCategory
        fields = ['name']
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)