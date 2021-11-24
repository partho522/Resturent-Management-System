from django.contrib import admin
from .models import Employee,Bill

# Register your models here.
admin.site.register(Employee)
admin.site.register(Bill)