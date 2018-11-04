from django import forms
class loginForm(forms.Form):
    uid=forms.EmailField(label='uid')
    password=forms.CharField(label='password',widget=forms.PasswordInput)
class regpatientForm(forms.Form):
    fn=forms.CharField(label='fn',max_length='30')
    ln=forms.CharField(label='ln',max_length='30')
    uid=forms.EmailField(label='uid')
    dob=forms.DateField(widget=forms.DateInput(format="%m/%d/%Y"))
    address=forms.CharField(max_length='100')
    city=forms.CharField(max_length='30')
    state=forms.CharField(max_length='30')
    country=forms.CharField(max_length='30')
    CHOICES={('1','FEMALE'),('2','MALE')}
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    password=forms.CharField(label='password',widget=forms.PasswordInput)
class verfForm(forms.Form):
    otp=forms.CharField(max_length=6)
class forgotForm1(forms.Form):
    uid=forms.EmailField(label='uid')
class forgotForm2(forms.Form):
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    otp=forms.CharField(max_length=6)
class udpForm(forms.Form):
     file = forms.FileField(widget=forms.FileInput(attrs={'onchange':'readURL(this)','style':'display:none','accept':'image/*'}))



#
