from django.db import models
class msg(models.Model):
    suid=models.CharField(max_length=100,blank=False,null=False)
    ruid=models.CharField(max_length=100,blank=False,null=False)
    msg=models.CharField(max_length=100,null=True,blank=True)
    imgmsg=models.CharField(max_length=100,null=True,blank=True)
    docmsg=models.CharField(max_length=100,null=True,blank=True)
    msgtime=models.DateTimeField(auto_now=True)
