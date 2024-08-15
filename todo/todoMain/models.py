from django.db import models

# Create your models here.
class TodoModel(models.Model):
    Title=models.CharField(max_length=30)
    Description=models.CharField(max_length=100)
    Date=models.DateField()
    Image=models.ImageField(upload_to="todoImages",null=True)
    Status=models.CharField(max_length=10,default='Pending...')
