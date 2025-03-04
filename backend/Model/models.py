from django.db import models

# Create your models here.
class Model(models.Model):
    model_id = models.BigAutoField(primary_key=True)
    algorithm_name = models.CharField(max_length=100,blank=False)
    model_description = models.CharField(max_length=1000,blank=False)
    model_url = models.CharField(max_length=1000,blank=False)
    data_type = models.CharField(max_length=100,blank=False,default='')
    task_type = models.CharField(max_length=100,blank=False)