from django.db import models
from loginDoctor.models import spec
class Symtoms(models.Model):
    symtm1=models.CharField(blank=False,null=False,max_length=50)
    symtm2=models.CharField(blank=False,null=False,max_length=50)
    spec=models.ForeignKey(spec,models.CASCADE)



# Create your models here.
