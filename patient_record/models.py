from django.db import models
from login2.models import user
from loginDoctor.models import Doctor
class patient_record(models.Model):
    pid=models.ForeignKey(user,models.CASCADE)
    did=models.ForeignKey(Doctor,models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    comment=models.CharField(max_length=1000,blank=False,null=False)
    disease=models.CharField(max_length=100,blank=False,null=False)
