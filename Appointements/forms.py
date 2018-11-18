from django import forms
from .models import Appointments

SLOT_CHOICES=[
    ('slot1','9:00 Am'),
('slot2','3:00 Pm'),
('slot3','7:00 Pm'),
]

class FormName(forms.Form):
    loc=forms.CharField()
    cat=forms.CharField()

#class slotform(forms.Form):
#    slot = forms.CharField(label="Choose Slot", widget=forms.Select(choices=SLOT_CHOICES))

class AppForm(forms.Form):
    doc_name = forms.CharField(max_length=30)
    fees = forms.IntegerField()
    rating = forms.IntegerField()
    date=forms.DateField()
    #slot=forms.CharField()
