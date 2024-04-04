from django.db import models

# Create your models here.
class Model(models.Model):
    model_id = models.BigAutoField(primary_key=True)
    model_name = models.CharField(max_length=100,blank=False)
    model_description = models.CharField(max_length=10000,blank=False)
    model_url = models.CharField(max_length=1000,blank=False)
    task_type = models.CharField(max_length=100,blank=False)