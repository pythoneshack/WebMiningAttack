from django.db import models

# Create your models here.


class Log(models.Model):
     title = models.CharField(max_length=100)
     csv = models.FileField(upload_to='logs/csvs/')

     def _str_(self):
       return self.title

