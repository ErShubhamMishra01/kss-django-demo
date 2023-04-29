from django.db import models

class Registration(models.Model):
    name=models.TextField(max_length=50)
    gender=models.TextField(max_length=50)
    email=models.TextField(max_length=50)
    course=models.TextField(max_length=50)
    address=models.TextField(max_length=50)
    