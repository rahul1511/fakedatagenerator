from django.db import models

# Create your models here.
class FakeGen(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    location=models.CharField(max_length=50)
    dob=models.DateField(max_length=20)
    salary=models.DecimalField(max_digits=20, decimal_places=2)
    
    

