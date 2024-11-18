from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','password']