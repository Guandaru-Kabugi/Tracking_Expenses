from rest_framework import serializers
from .models import Category, Item
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Name of the Category cannot be Less than 4 characters")
        return value
class ExpenseSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='item_category.name', read_only=True)
    class Meta:
        model = Item
        fields = ['id','item_name','item_category','date_recorded','cost']
    def validate_item_name(self, value):
        if len(value) <4:
            raise serializers.ValidationError('Name of Item cannot be less than 4 characters')
        return value
    
class ItemSerializer(serializers.ModelSerializer):
    # Define the item_category field
    item_category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.none(), required=True)

    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_category', 'cost']

    def __init__(self, *args, **kwargs):
        # Get the user from the context (which is passed in the view)
        user = kwargs.get('context', {}).get('request', {}).user
        super().__init__(*args, **kwargs)

        if user:
            # Filter the categories to show only those created by the current user
            self.fields['item_category'].queryset = Category.objects.filter(user=user)

# class ItemSerializer(serializers.ModelSerializer):
#     item_category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.none(),required=True)
#     item_category_name = serializers.CharField(source='item_category.name',read_only=True)

#     class Meta:
#         model = Item
#         fields = ['id', 'item_name', 'item_category', 'item_category_name','cost']
#     def __init__ (self, *args, **kwargs):

#         user = kwargs.get('context',{}).get('request',{}).user
#         super().__init__(*args,**kwargs)

#         if user:
#             self.fields['item_category'].queryset = Category.objects.filter(user=user)
