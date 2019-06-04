from django.db import models

# Create your models here.

class EmployeeTable(models.Model):
    E_firstname= models.CharField(max_length=10)
    E_lastname= models.CharField(max_length=10)
    E_id=models.IntegerField()

    def __str__(self):
        return self.E_firstname