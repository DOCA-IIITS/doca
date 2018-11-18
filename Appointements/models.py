from django.db import models
from loginDoctor.models import Doctor,spec
from login2.models import user
from datetime import datetime,date
from django.utils import timezone
# Create your models here.


#class slot(models.Model):
#    slot=models.CharField(max_length=6,default="slot1")


class Appointments(models.Model):
    doctor_id = models.ForeignKey(Doctor,models.CASCADE)
    date=models.DateField(null=False,blank=False)
    patient_id=models.ForeignKey(user,models.CASCADE)
 #   slot=models.ForeignKey(slot,on_delete=models.CASCADE)
