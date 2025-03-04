from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
import uuid

class User(AbstractBaseUser):
    user_id = models.BigAutoField(primary_key=True, verbose_name="用户ID")
    user_name = models.CharField(verbose_name = "用户姓名",max_length=50,unique=True,blank=False,default="user"+str(uuid.uuid4()))
    phone_number = PhoneNumberField(unique=True, null=False, blank=True)
    is_admin_or_not = models.BooleanField(verbose_name="是否为管理员",blank=False,default=False)
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['phone_number']
    class Meta:
        ordering = ['user_id']

