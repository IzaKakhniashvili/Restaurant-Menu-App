from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Restaurant, MainCategory, MenuCategory, Dish, Ingredient
from .serializers import (
    RestaurantSerializer,
    MainCategorySerializer,
    MenuCategorySerializer,
    MenuCategoryDetailSerializer
)
from .permissions import IsOwnerOrReadOnly

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MainCategoryView(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    
class MenuCategoryView(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    
class CategoryDetailView(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategoryDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    