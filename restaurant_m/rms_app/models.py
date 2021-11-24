from django.db import models
from django.db.models.lookups import PostgresOperatorLookup

# Create your models here.
class Employee(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Post = models.CharField(max_length=30)
    Phone = models.IntegerField()
    Salary = models.IntegerField()
    
    def __srt__(self):
        return self.Name

class Bill(models.Model):
    Order_or_Date = models.DateField(auto_now_add=True,blank=True)
    Order_or_Serial = models.IntegerField(primary_key=True)
    Amount = models.IntegerField()
    Bill_or_Status = models.CharField(max_length=20)

