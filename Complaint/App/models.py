from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complaint(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    phone=models.CharField(max_length=12)
    complaintText = models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

