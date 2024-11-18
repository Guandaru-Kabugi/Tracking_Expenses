from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password):
        if not email:
            raise ValueError('Ensure you have provided an email address')
        if not username:
            raise ValueError('Ensure you have given a username')
        if not first_name:
            raise ValueError('Ensure you have given a first name')
        if not last_name:
            raise ValueError('Ensure you have given a last name')
        user = self.model(email=self.normalize_email(email),first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name,email,password,username):
        user = self.create_user(email=self.normalize_email(email),username=username,first_name=first_name,last_name=last_name,password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True,null=False,verbose_name='Username')
    email = models.EmailField(max_length=200,unique=True,null=False,verbose_name='Email Address')
    first_name = models.CharField(max_length=70,unique=False,null=False,verbose_name='First Name')
    last_name = models.CharField(max_length=70,unique=False,null=False,verbose_name='Last Name')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = UserManager()


    def __str__(self):
        return self.username