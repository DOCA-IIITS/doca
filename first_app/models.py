from django.db import models

# Create your models here.
class category(models.Model):
    cat_name=models.CharField(max_length=36,unique=True)
    def __str__(self):
        return self.cat_name

class location(models.Model):
    loc_name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.loc_name

class doctor(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,)
    location=models.ForeignKey(location,on_delete=models.CASCADE)
    doc_name=models.CharField(max_length=30,unique=True)
    fees=models.IntegerField()
    rating=models.IntegerField()

class Appointments(models.Model):
    doc_name=models.CharField(max_length=30)
    fees=models.IntegerField()
    rating=models.IntegerField()