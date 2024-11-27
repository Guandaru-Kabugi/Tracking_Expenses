from django.shortcuts import render,get_object_or_404
from .serializers import ExpenseSerializer,CategorySerializer,ItemSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Item,Category
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,BasePermission
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ItemFilter
# Create your views here.
class SingleUserAccess(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
"""
CRUD Operations
"""

# best is to use modelviewset that allows crud operations
@permission_classes([IsAuthenticated])
class CategoryViewSet(ModelViewSet):
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    serializer_class = CategorySerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# @permission_classes([SingleUserAccess,IsAuthenticated])
# class ExpenseViewSet(ModelViewSet):
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['item_name','item_category','date_recorded','cost']
#     def get_queryset(self):
#         return Item.objects.filter(user=self.request.user)
#     serializer_class = ExpenseSerializer
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
@permission_classes([SingleUserAccess,IsAuthenticated])
class ExpenseViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['item_name','item_category','date_recorded','cost']
    filterset_class = ItemFilter
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        # Pass the request context to the serializer to get the current user
        context = super().get_serializer_context()
        context['request'] = self.request
        return context