from rest_framework import serializers


class ExpenseCalculateSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    item_name = serializers.CharField(required=False)
    item_category = serializers.CharField(required=False)

    # we validate to ensure start date is below end date

    def validate(self, data):
        if 'start_date' in data and 'end_date' in data and data['start_date'] > data['end_date']:
            raise serializers.ValidationError('Start date cannot be greater than end date')
        return data