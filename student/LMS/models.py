from django.db import models
from django.contrib import admin
class LMS(models.Model):
    student_name=models.CharField(max_length=20)
    reg_num=models.IntegerField()
    age_num=models.IntegerField()
    date_of_birth=models.DateField()

class LMSAdmin(admin.ModelAdmin):
    list_display=('student_name', 'reg_num', 'age_num', 'date_of_birth')
# Create your models here.
