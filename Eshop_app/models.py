from django.db import models

# Create your models here.
class shop(models.Model):
    img=models.ImageField(upload_to='picture/')
    name=models.CharField(max_length=100)
    price=models.IntegerField()

