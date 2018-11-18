from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Rating.models import Doctor,Review
from Rating.forms import ReviewForm,DoctorForm
from Rating import forms
from django.shortcuts import get_object_or_404
from loginDoctor.models import Doctor
from login2.models import user
import numpy as np
from django.db.models import Count,Avg,Max
from django.db.models import IntegerField
from login2.models import user
from loginDoctor.models import Doctor

def review(request):
    rate = Review.objects.all()
    if ('uid' in request.session)and ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:

             if request.method == 'POST':
                f = ReviewForm(request.POST)
                review_details = Review.objects.order_by('pub_date')
                if f.is_valid():
                    comment=f.cleaned_data['comment']
                    rating=f.cleaned_data['rating']
                    uSer=user.objects.get(uid=request.session['uid'])
                    doCtor=Doctor.objects.get(uid='avinashkatariya810@gmail.com')
                    Review(patient_id=uSer,doctor_id=doCtor,comment=comment,rating=rating).save()
        return render(request,'ratings/temp/review.html',{'form':ReviewForm()})
    return HttpResponseRedirect('/login/login/')

