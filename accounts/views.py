from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateUserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

# I decided to use createapiview to create a new user into my mysql database
class CreateNewUser(CreateAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(User,email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            return Response({"user":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"errors":serializer.errors},status.HTTP_400_BAD_REQUEST)
# Used a function based view to login in the user. The user can also use the details to access token
@api_view(['POST'])     
def login(request):
    user = get_object_or_404(User,email=request.data['email'])
    if user:
        if user.check_password(request.data['password']):
            serializer = CreateUserSerializer(instance=user)
            return Response({"user":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"errors":serializer.errors},status=status.HTTP_401_UNAUTHORIZED)