from django.db import models
from Task.models import Task
from User.models import User

# Create your models here.
class Data(models.Model):
    data_id = models.BigAutoField(primary_key=True)
    data_type = models.CharField(max_length=100,blank=False)
    data_algorithm = models.CharField(max_length=100,blank=False,default='')
    ori_data_url = models.CharField(max_length=1000,default='')
    cleaned_data_url = models.CharField(max_length=1000,default='')
    marked_data_url = models.CharField(max_length=1000,default='')
    preprocessed_data_url = models.CharField(max_length=1000,default='')
    marked_preprocessed_data_url = models.CharField(max_length=1000,default='')
    data_description = models.CharField(max_length=1000,blank=False,default='',unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=100,blank=False,default='')

class Result(models.Model):
    result_id = models.BigAutoField(primary_key=True)
    result_url = models.CharField(max_length=1000,blank=False)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

class ori_data_cols(models.Model):
    data_id = models.ForeignKey(Data, on_delete=models.CASCADE)
    cols = models.CharField(max_length=10000,blank=False)