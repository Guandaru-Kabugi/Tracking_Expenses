from django.db import models
from django.db.models.signals import post_delete
from taggit.managers import TaggableManager
from django.dispatch import receiver
from taggit.models import Tag
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
#Create category

class Category(models.Model):
    name = models.CharField(max_length=100,unique=False,null=False, blank=False, verbose_name='Item Category')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='user',null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
# we create the expense model
class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,default=None)
    item_name = models.CharField(max_length=100,unique=False,verbose_name='Item Name')
    item_category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Item_Category', null=False)
    date_recorded = models.DateField(auto_now_add=True, verbose_name='Date Added')
    cost = models.DecimalField(decimal_places=2,max_digits=7,verbose_name='Cost of Item')


    def __str__(self):
        return f'{self.user.first_name} bought {self.item_name}'
    

    tags = TaggableManager()

@receiver(post_delete, sender=Item)
def delete_unused_tags(sender, instance, **kwargs):
    for tag in instance.tags.all():
        if not tag.taggit_taggeditem_items.exists():
            tag.delete()
