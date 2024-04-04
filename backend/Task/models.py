from django.db import models
from User.models import User

# Create your models here.
class Task(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=100,blank=False)
    task_type = models.CharField(max_length=100,blank=False)
    task_state = models.CharField(max_length=100,blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)