from django.db import models

# Create your models here.

class Student(models.Model):
    gen = [("FEMALE","FEMALE"),("MALE","MALE"),("OTHER","OTHER")]
    stu_id = models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=30,choices=gen)
    course = models.CharField(max_length=30)
    email = models.EmailField(unique=True)



