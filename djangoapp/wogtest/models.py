from django.db import models

# Create your models here.

class table1(models.Model):
    userid = models.CharField(max_length=30)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=30)
    price = models.IntegerField()
    year = models.IntegerField()
    county_name = models.CharField(max_length=30)
    state_code = models.CharField(max_length=30)
    state_name = models.CharField(max_length=30)
