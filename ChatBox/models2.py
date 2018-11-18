from django.db import models
class file_save(models.Model):
    pid=models.CharField(max_length=100,blank=False,null=False)
    did=models.CharField(max_length=100,blank=False,null=False)
    date=models.DateTimeField(auto_now=True)
    file_path=models.CharField(max_length=200,blank=False,null=False)
