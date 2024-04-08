from django.db import models

# Create your models here.
class Student_details(models.Model):
    name=models.CharField(max_length=100)
    Class= models.TextField()
    year= models.IntegerField()
    rep_before= models.BooleanField(default=False)
    select= models.BooleanField(default=False)
    responsibilities= models.TextField()
    have_responsibilities=models.BooleanField(default=False)
    responsibilities=models.TextField()
