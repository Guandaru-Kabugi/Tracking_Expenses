from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Category
User = get_user_model()
# Create your tests here.


class TestViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_url = reverse('category-list')
        self.expense_url = reverse('expenses-list')
        new_user = User.objects.create_superuser(
            username='John',
            email= 'john@gmail.com',
            first_name = 'John',
            last_name = 'Guandaru',
            password='Michael123.'
        )
        new_user_2 = User.objects.create_user(
            username='James',
            email= 'james@gmail.com',
            first_name = 'James',
            last_name = 'Kabugi',
            password='Michael123.'
        )
        self.client.login(email='john@gmail.com',password='Michael123.')
        new_category = self.client.post(self.category_url,
                                    {
                                        'name':'proteins'
                                    })
        self.client.logout
    def test_category(self):
        self.client.login(email='john@gmail.com',password='Michael123.')
        response = self.client.post(self.category_url,
                                    {
                                        'name':'groceries'
                                    })
        print(response.data)
        self.client.logout
    def test_expense(self):
        self.client.login(email='john@gmail.com',password='Michael123.')
        user = User.objects.get(email='john@gmail.com')
        category = Category.objects.get(name='proteins')
        print(f'category: {category}')

        response = self.client.post(self.expense_url,
                                    {
                                        'item_name':'beef',
                                        'item_category':category.id,
                                        'cost':200.00

                                    })
        print(f'expense data: {response.data}')
        self.client.logout