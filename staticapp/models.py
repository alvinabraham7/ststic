from django.db import models

# Create your models here.
class football(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='jpg')
    desc=models.TextField()



