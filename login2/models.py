from django.db import models
class user(models.Model):
    fname=models.CharField(max_length=50,null=False,blank=False)
    lname=models.CharField(max_length=50,null=False,blank=False)
    uid=models.EmailField(primary_key=True,max_length=50,null=False,blank=False)
    dob=models.DateField(null=False,blank=False)
    gender=models.CharField(max_length=1,null=False,blank=False)
    address=models.CharField(max_length=100,null=False,blank=False)
    city=models.CharField(max_length=25,null=False,blank=False)
    state=models.CharField(max_length=25,null=False,blank=False)
    country=models.CharField(max_length=25,null=False,blank=False)
    password=models.CharField(max_length=50,null=False,blank=False)
    dp=models.CharField(max_length=100,default='uploads/A@DOCA@IIIT@DPdefualt.png')
    def full_name(self):
        return self.fname+' '+self.lname
    def Gender(self):
        if self.gender==1:
            return 'FEMALE'
        return 'MALE'
class userApplied(models.Model):
    fname=models.CharField(max_length=50,null=False,blank=False)
    lname=models.CharField(max_length=50,null=False,blank=False)
    uid=models.EmailField(primary_key=True,max_length=50,null=False,blank=False)
    dob=models.DateField(null=False,blank=False)
    gender=models.CharField(max_length=1,null=False,blank=False)
    address=models.CharField(max_length=100,null=False,blank=False)
    city=models.CharField(max_length=25,null=False,blank=False)
    state=models.CharField(max_length=25,null=False,blank=False)
    country=models.CharField(max_length=25,null=False,blank=False)
    password=models.CharField(max_length=50,null=False,blank=False)
    otp=models.IntegerField()
# Create your models here.
class userF(models.Model):
    uid=models.EmailField(primary_key=True,max_length=50,null=False,blank=False)
    otp=models.IntegerField()
