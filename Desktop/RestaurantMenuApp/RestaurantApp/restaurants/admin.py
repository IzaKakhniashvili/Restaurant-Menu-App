from django.contrib import admin
from .models import Restaurant,  MenuCategory, MainCategory, Dish, Ingredient
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(MainCategory)
admin.site.register(Dish)
admin.site.register(Ingredient)