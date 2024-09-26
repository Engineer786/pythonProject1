from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job = models.CharField(max_length=60)
    company = models.CharField(max_length=60)