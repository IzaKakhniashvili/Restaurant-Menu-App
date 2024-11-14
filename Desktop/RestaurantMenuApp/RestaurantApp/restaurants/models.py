from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number =PhoneNumberField()
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    user = models.ForeignKey(User, related_name='restaurants', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, related_name='main_categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main_categories/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(MainCategory, related_name = 'menu_categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_categories/', null = True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='dishes')
    image = models.ImageField(upload_to='dishes/', null=True, blank = True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')
    
    def __str__(self):
        return self.name