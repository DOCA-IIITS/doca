from django import forms
from first_app.models import Appointments

class FormName(forms.Form):
    loc=forms.CharField()
    cat=forms.CharField()

class AppForm(forms.ModelForm):
    class Meta():
        model=Appointments
        fields='__all__'
