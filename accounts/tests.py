from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class TestAccountViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup = reverse('signup')
        self.login = reverse('login')
        new_user = self.client.post(self.signup,
            {
            "username":"John",
            "email":"john@gmail.com",
            "password":"Michaelalx123.",
            "first_name":"John",
            "last_name":"Manan",
            })
    def test_signup_view(self):
        response = self.client.post(self.signup,
            {
            "username":"Michael",
            "email":"michael@gmail.com",
            "password":"Michaelalx123.",
            "first_name":"Michael",
            "last_name":"Maina",
            }
            )
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_login_view(self):
        response = self.client.post(self.login,
            {
                "email":"john@gmail.com",
                "password":"Michaelalx123."
            }
                                    )
        print(f"The new login data: {response.data}")
