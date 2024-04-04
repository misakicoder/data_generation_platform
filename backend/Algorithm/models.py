from django.db import models

# Create your models here.
class Algorithm(models.Model):
    algorithm_id = models.BigAutoField(primary_key=True)
    algorithm_name = models.CharField(max_length=100,blank=False)
    algorithm_description = models.CharField(max_length=10000,blank=False)
    task_type = models.CharField(max_length=100,blank=False)


