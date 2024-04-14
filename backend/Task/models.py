from django.db import models
from User.models import User

# Create your models here.
class Task(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=100,blank=False)
    task_type = models.CharField(max_length=100,blank=False)
    task_algorithm = models.CharField(max_length=100,blank=False,default='')
    task_state = models.CharField(max_length=100,blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    result_id = models.IntegerField(default=0)

class DataManager(models.Model):
    data_clean = models.BooleanField(default=False)
    data_mark = models.BooleanField(default=False)
    data_preprocess = models.BooleanField(default=False)
    data_generate = models.BooleanField(default=False)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)