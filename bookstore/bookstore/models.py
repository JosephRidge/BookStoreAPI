from django.db import models 

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    bookImage = models.CharField(max_length=500)
    category = models.CharField(max_length=200)
    favorite = models.BooleanField()
    pages = models.IntegerField()
    authors =  models.CharField(max_length=500)
#  Return a valid name 
    def __str__(self):
        return self.name +""