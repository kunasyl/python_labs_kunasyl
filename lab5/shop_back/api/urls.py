from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = router.urls

# urlpatterns = [
    # path('products/', views.ProductView.as_view({'get':'list'})), #Список всех продуктов
    # path('products/<int:pk>/', views.ProductView.as_view({'get':'retrieve'})), #Получить один продукт
    # path('categories/', views.CategoryView.as_view({'get':'list'})), #Список всех категорий
    # path('categories/<int:pk>', views.CategoryView.as_view({'get':'retrieve'})), #Получить одну категорию
    # path('categories/<int:id>/products/'), #Список продуктов по категориям
# ]