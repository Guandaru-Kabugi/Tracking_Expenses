from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'expense', views.ExpenseViewSet, basename='expenses')
urlpatterns = [
    path('',include(router.urls)),
]