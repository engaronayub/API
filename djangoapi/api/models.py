from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 250)
    language =  models.CharField(max_length = 250)
    price =  models.CharField(max_length = 10)
    description = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.name




# Create your models here.
