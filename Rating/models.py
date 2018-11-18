from django.db import models
import numpy as np
from datetime import date
from datetime import datetime
from login2.models import user
from loginDoctor.models import Doctor
from login2.models import  user


class Review(models.Model):
    doctor_id = models.ForeignKey(Doctor,models.CASCADE)
    patient_id = models.ForeignKey(user,models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length=200,null=True)
    rating = models.IntegerField()


def __str__(self):
    id = self.doctor_id
    return (id)
