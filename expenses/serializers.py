from rest_framework import serializers
from .models import Category,Item
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Name of the Category cannot be Less than 4 characters")
        return value
class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='item_category.name', read_only=True)
    class Meta:
        model = Item
        fields = ['id','user','item_name','item_category','category','date_recorded','cost']
    def validate_item_name(self, value):
        if len(value) <4:
            raise serializers.ValidationError('Name of Item cannot be less than 4 characters')
        return value