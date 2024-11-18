from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
# first we create categories
class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,default=None)
    name = models.CharField(max_length=100,unique=True,null=False,verbose_name='Expense Category')

    def __str__(self):
        return self.name
# we create the expense model
class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,default=None)
    item_name = models.CharField(max_length=100,unique=False,verbose_name='Item Name')
    item_category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Item Category')
    date_recorded = models.DateField(auto_now_add=True, verbose_name='Date Added')
    cost = models.DecimalField(decimal_places=2,max_digits=7,verbose_name='Cost of Item')


    def __str__(self):
        return f'{self.user.first_name} bought {self.item_name}'