from django.shortcuts import render
from .serializers import ExpenseCalculateSerializer
from rest_framework.views import APIView
from django.db.models import Sum
from expenses.models import Item
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TrackExpenses(APIView):
    def post(self,request):
        serializer = ExpenseCalculateSerializer(data=request.data)
        if serializer.is_valid():
            start_date = serializer.validated_data.get('start_date')
            end_date = serializer.validated_data.get('end_date')
            item_name = serializer.validated_data.get('item_name')
            item_category = serializer.validated_data.get('item_category')

            items_for_current_user = Item.objects.filter(user=self.request.user)
            if start_date:
                items_for_current_user = items_for_current_user.filter(date_recorded__gte=start_date) #greater than or equal to
            if end_date:
                items_for_current_user = items_for_current_user.filter(date_recorded__lte=end_date) #less than or equal to
            if item_name:
                items_for_current_user = items_for_current_user.filter(item_name__icontains=item_name)
            if item_category:
                items_for_current_user = items_for_current_user.filter(item_category__name__icontains=item_category)
            total_expenditure = items_for_current_user.aggregate(total_cost=Sum('cost'))['total_cost'] or 0 #we get total cost and extracts dictionary key total cost from aggregate

            response_data = {
                'total_expenditure': total_expenditure,
                'start_date': start_date,
                'end_date': end_date,
                'item_name': item_name,
                'item_category': item_category,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
