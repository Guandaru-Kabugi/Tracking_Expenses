from rest_framework import serializers
from .models import Category, Item
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
class CategorySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Category
        fields = ['id','name','tags']
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Name of the Category cannot be Less than 4 characters")
        return value
class ExpenseSerializer(TaggitSerializer, serializers.ModelSerializer):
    # category = serializers.CharField(source='item_category.name', read_only=True)
    tags = TagListSerializerField()
    class Meta:
        model = Item
        fields = ['id','item_name','item_category','date_recorded','cost','tags']
    def validate_item_name(self, value):
        if len(value) <4:
            raise serializers.ValidationError('Name of Item cannot be less than 4 characters')
        return value
    
class ItemSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    # Define the item_category field
    item_category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.none(), required=True)

    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_category', 'cost','tags']

    def __init__(self, *args, **kwargs):
        # Get the user from the context (which is passed in the view)
        user = kwargs.get('context', {}).get('request', {}).user
        super().__init__(*args, **kwargs)

        if user:
            # Filter the categories to show only those created by the current user
            self.fields['item_category'].queryset = Category.objects.filter(user=user)
            
    def to_internal_value(self, data):
        # Create a mutable copy of the data
        mutable_data = data.copy()

        # Split the tags field if it's provided as a single string
        tags = mutable_data.get('tags')
        if isinstance(tags, str):
            mutable_data['tags'] = [tag.strip() for tag in tags.split(',')]

        return super().to_internal_value(mutable_data)
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
