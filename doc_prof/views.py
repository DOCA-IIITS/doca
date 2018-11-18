from django.shortcuts import render
from loginDoctor.models import Doctor,DoctorApplied
from django.http import HttpResponseRedirect
from loginDoctor.form import loginDocForm, regDocForm, verfDocForm, udpDocForm
import random
from login2.views2 import send_otp
import os
from django.conf import settings
from django.core.files.storage import default_storage

def index(request):
    return render(request,'doc_prof/basic.html')

def register(request):
    form=regDocForm()
    if request.method == 'POST':
        form=regDocForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['rpass']:
                return render(request,'doc_prof/register.html',{'form':form,'errp':'Passwords do not match!'})
            if Doctor.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                return render(request,'doc_prof/register.html',{'form':form, 'erru':'User ID already exists!'})
            otp=random.randint(100000,999999)
            t=DoctorApplied(fname=form.cleaned_data['fn'],lname=form.cleaned_data['ln'],uid=form.cleaned_data['uid'].lower(),dob=form.cleaned_data['dob'],
            password=form.cleaned_data['password'],otp=otp,gender=form.cleaned_data['gender'],city=form.cleaned_data['city'],
            address=form.cleaned_data['address'],state=form.cleaned_data['state'],country=form.cleaned_data['country'],Specilazation=form.cleaned_data['Specialisation'])
            t.save()
            send_otp(form.cleaned_data['uid'],otp)
            return HttpResponseRedirect('/doc/verf?uidc='+form.cleaned_data['uid'])
        else:
            return render(request,'doc_prof/register.html',{'form':form})
    return render(request,'doc_prof/register.html',{'form':form})

def verf(request):
    uidc=request.GET.get('uidc','')
    if request.method == 'GET' and 'resend' in request.GET:
        uidc=request.GET.get('uidc','')
        print(1)
        if DoctorApplied.objects.filter(uid=uidc.lower()).count()==1:
            otp=random.randint(100000,999999)
            print(otp)
            send_otp(uidc,otp)
            a=DoctorApplied.objects.get(uid=uidc.lower())
            print(a.otp)
            a.otp=otp
            a.save()
            print(a.otp)
            return render(request,'doc_prof/verf.html',{'uidc':uidc})
        else:
            return render(request,'doc_prof/verf.html',{'err3':'OOPS! Something went wrong!'})
    if request.method == 'GET' and 'verify' in request.GET:
        uidc=request.GET.get('uidc','')
        if DoctorApplied.objects.filter(uid=uidc.lower()).count()==1:
            a=DoctorApplied.objects.get(uid=uidc.lower())
            b=a.otp
            otp=request.GET.get("o1",0)+request.GET.get("o2",0)+request.GET.get("o3",0)+request.GET.get("o4",0)+request.GET.get("o5",0)+request.GET.get("o6",0)
            if otp == str(b) :
                b=Doctor(fname=a.fname,lname=a.lname,uid=a.uid,dob=a.dob,password=a.password,
                gender=a.gender,city=a.city,address=a.address,state=a.state,country=a.country,Specilazation=a.Specilazation)
                b.save()
                request.session['uid']=uidc.lower()
                request.session['pwd']=a.password
                a.delete()
                return HttpResponseRedirect('/doc/udp/')
            else:
                return render(request,'doc_prof/verf.html',{'err1':'Invalid otp!','uidc':uidc})
        else:
            return render(request,'doc_prof/verf.html',{'err2':'OOPS! Something went wrong!'})
    return render(request,'doc_prof/verf.html',{'uidc':uidc})

def udp(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count()==1:
            a=Doctor.objects.get(uid=request.session['uid'])
            if request.session['pwd']==a.password:
                if request.method == 'POST':
                    save_path = os.path.join(settings.MEDIA_ROOT, 'static/uploads',request.POST.get('file',''))
                    print(request.POST)
                    print(request.POST.get('file',''))
                    path = default_storage.save(save_path, request.FILES['file'])

                    save_path=save_path+'/'+request.session['uid']+'.png'
                    try:
                        os.rename(path,save_path)
                    except FileExistsError:
                        os.remove(save_path)
                        os.rename(path,save_path)
                    a=Doctor.objects.get(uid=request.session['uid'].lower())
                    a.dp=save_path
                    a.save()
                    return HttpResponseRedirect('/doc/logout/')
                else:
                    return render(request, 'doc_prof/udp.html')
    return HttpResponseRedirect('/doc/login/')

def login(request):
    if request.method == 'POST':
        form=loginDocForm(request.POST)
        if form.is_valid():
            uid=form.cleaned_data['uid'].lower()
            if Doctor.objects.filter(uid=uid).count()==1:
                db=Doctor.objects.get(uid=uid)
                if form.cleaned_data['password'] == db.password:
                    request.session['uid']=uid
                    request.session['pwd']=db.password
                    return HttpResponseRedirect('/doc/home')
                else:
                    return render(request,'doc_prof/login.html',{'form':form , 'errp':'Incorrect Password!'})
            else:
                return render(request,'doc_prof/login.html',{'form':form, 'erru':'Username doesn\'t exist!'})
        else:
            return render(request,'doc_prof/login.html',{'form':form,'errs':form.errors})
    else:
        if ('uid' in request.session) & ('pwd' in request.session):
            return HttpResponseRedirect('/doc/home')
        form=loginDocForm()
    return render(request,'doc_prof/login.html',{'form':form})


def home(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count()==1:
            db=Doctor.objects.get(uid=request.session['uid'])
            return render(request,'doc_prof/dhome.html',{'fname':db.fname,'dp':db.dp[7::]})
    return HttpResponseRedirect('/doc/login')

def profile(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count()==1:
            db=Doctor.objects.get(uid=request.session['uid'])
            return render(request,'doc_prof/dprofile.html',{'db':db,'pp':db.dp[7::], 'gender':db.Gender()})
    return HttpResponseRedirect('/doc/login')

def logout(request):
    del request.session['uid']
    del request.session['pwd']
    return HttpResponseRedirect('/doc/login')
