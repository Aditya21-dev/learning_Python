from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    document = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.name +" "+ self.password
    