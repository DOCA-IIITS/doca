from django import forms
# from .models import user,equationlog
from django.core import validators
from .models import patient_record
#
# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("NAME SHLD START WITH Z")
#

class UserForm(forms.ModelForm):
    class Meta():
        model=patient_record
        fields = [ 'comment', 'disease']




# def clean_botcatcher(self):
#     botcatcher=self.cleaned_data['botcatcher']
#     if(len(botcatcher)) > 0:
#         raise forms.ValidationError("gotcha bot");
#     return botcatcher
