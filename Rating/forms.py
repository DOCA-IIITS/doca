from django import forms
from django.forms import ModelForm,Textarea
from Rating.models import Doctor,Review
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS


class DoctorForm(ModelForm):
    class meta:
        model = Doctor
        fields = ['pub_date','doctor_name']


class ReviewForm(forms.Form):
    comment= forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    rating=forms.IntegerField()

