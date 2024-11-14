from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RestaurantView, MainCategoryView, MenuCategoryView, CategoryDetailView


app_name = 'restaurants'


router = DefaultRouter()
router.register(r'restaurants', RestaurantView, basename='restaurant')
router.register(r'main-categories', MainCategoryView, basename='main_category' )
router.register(r'menu-categories', MenuCategoryView, basename='subcategory')
router.register(r'dishes', CategoryDetailView, basename='detail_view')

urlpatterns = [
    path('', include(router.urls)),
]