# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Student Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 students

## PROGRAM
```
models.py 
from django.db import models
from django.contrib import admin
class LMS(models.Model):
    student_name=models.CharField(max_length=20)
    reg_num=models.IntegerField()
    age_num=models.IntegerField()
    date_of_birth=models.DateField()

class LMSAdmin(admin.ModelAdmin):
    list_display=('student_name', 'reg_num', 'age_num', 'date_of_birth')
admin.py
from django.contrib import admin
from.models import LMS,LMSAdmin
admin.site.register(LMS,LMSAdmin)
```
## OUTPUT
![alt text](<Screenshot 2025-11-25 110653.png>)
 ![alt text](<Screenshot 2025-11-25 110723.png>)
## RESULT
Thus the program for creating Student database using ORM hass been executed successfully
