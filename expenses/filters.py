import django_filters
from .models import Item
#here, I learned that we can implement a custom filter using django_filters.filterset
#I am filtering through numbers, which is why I have Numberfilter
class ItemFilter(django_filters.FilterSet):
    item_name = django_filters.CharFilter(field_name='item_name', lookup_expr='icontains')
    #like in serializers, I get the model and also the fields which will be passed as filter_class
    item_category = django_filters.NumberFilter(field_name='item_category', lookup_expr='exact')  # Case-insensitive exact match
    date_recorded = django_filters.DateFilter(field_name='date_recorded',lookup_expr='icontains')
    cost = django_filters.NumberFilter(field_name='cost',lookup_expr='icontains')

    class Meta:
        model = Item
        fields = ['item_name', 'item_category','date_recorded','cost']
