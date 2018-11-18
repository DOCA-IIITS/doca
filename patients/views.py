from django.shortcuts import render
from login2.models import user, userApplied
from django.http import HttpResponseRedirect
from login2.form import loginForm, regpatientForm, verfForm, udpForm
import random
from login2.views2 import send_otp
import os
from django.conf import settings
from django.core.files.storage import default_storage

def register(request):
    form=regpatientForm()
    if request.method == 'POST':
        form=regpatientForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['rpass']:
                return render(request,'patients/register.html',{'form':form,'errp':'Passwords do not match!'})
            if user.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                return render(request,'patients/register.html',{'form':form, 'erru':'User ID already exists!'})
            otp=random.randint(100000,999999)
            t=userApplied(fname=form.cleaned_data['fn'],lname=form.cleaned_data['ln'],uid=form.cleaned_data['uid'].lower(),dob=form.cleaned_data['dob'],
            password=form.cleaned_data['password'],otp=otp,gender=form.cleaned_data['gender'],city=form.cleaned_data['city'],
            address=form.cleaned_data['address'],state=form.cleaned_data['state'],country=form.cleaned_data['country'])
            t.save()
            send_otp(form.cleaned_data['uid'],otp)
            return HttpResponseRedirect('/pat/verf?uidc='+form.cleaned_data['uid'])
        else:
            return render(request,'patients/register.html',{'form':form})
    return render(request,'patients/register.html',{'form':form})

def verf(request):
    uidc=request.GET.get('uidc','')
    if request.method == 'GET' and 'resend' in request.GET:
        uidc=request.GET.get('uidc','')
        print(1)
        if userApplied.objects.filter(uid=uidc.lower()).count()==1:
            otp=random.randint(100000,999999)
            print(otp)
            send_otp(uidc,otp)
            a=userApplied.objects.get(uid=uidc.lower())
            print(a.otp)
            a.otp=otp
            a.save()
            print(a.otp)
            return render(request,'patients/verf.html',{'uidc':uidc})
        else:
            return render(request,'patients/verf.html',{'err3':'OOPS! Something wrong!'})
    if request.method == 'GET' and 'verify' in request.GET:
        uidc=request.GET.get('uidc','')
        print(userApplied.objects.filter(uid=uidc.lower()).count())
        if userApplied.objects.filter(uid=uidc.lower()).count()==1:
            a=userApplied.objects.get(uid=uidc.lower())
            b=a.otp
            otp=request.GET.get("o1",0)+request.GET.get("o2",0)+request.GET.get("o3",0)+request.GET.get("o4",0)+request.GET.get("o5",0)+request.GET.get("o6",0)
            if otp == str(b) :
                b=user(fname=a.fname,lname=a.lname,uid=a.uid,dob=a.dob,password=a.password,
                gender=a.gender,city=a.city,address=a.address,state=a.state,country=a.country)
                b.save()
                request.session['uid']=uidc.lower()
                request.session['pwd']=a.password
                a.delete()
                return HttpResponseRedirect('/pat/udp/')
            else:
                return render(request,'patients/verf.html',{'err1':'Invalid otp!','uidc':uidc})
        else:
            return render(request,'patients/verf.html',{'err2':'OOPS! Something went wrong!'})
    return render(request,'patients/verf.html',{'uidc':uidc})

def udp(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            a=user.objects.get(uid=request.session['uid'])
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
                    a=user.objects.get(uid=request.session['uid'].lower())
                    a.dp=save_path
                    a.save()
                    return HttpResponseRedirect('/pat/logout/')
                else:
                    return render(request, 'patients/udp.html')
    return HttpResponseRedirect('/pat/login/')

def login(request):
    if request.method == 'POST':
        form=loginForm(request.POST)
        if form.is_valid():
            uid=form.cleaned_data['uid'].lower()
            if user.objects.filter(uid=uid).count()==1:
                db=user.objects.get(uid=uid)
                if form.cleaned_data['password'] == db.password:
                    request.session['uid']=uid
                    request.session['pwd']=db.password
                    return HttpResponseRedirect('/pat/home')
                else:
                    return render(request,'patients/login.html',{'form':form , 'errp':'Incorrect Password!'})
            else:
                return render(request,'patients/login.html',{'form':form, 'erru':'Username doesn\'t exist!'})
        else:
            return render(request,'patients/login.html',{'form':form,'errs':form.errors})
    else:
        if ('uid' in request.session) & ('pwd' in request.session):
            return HttpResponseRedirect('/pat/home')
        form=loginForm()
    return render(request,'patients/login.html',{'form':form})


def home(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            db=user.objects.get(uid=request.session['uid'])
            return render(request,'patients/phome.html',{'fname':db.fname,'dp':db.dp[7::]})
    return HttpResponseRedirect('/pat/login')

def profile(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            db=user.objects.get(uid=request.session['uid'])
            return render(request,'patients/pprofile.html',{'db':db,'pp':db.dp[7::], 'gender':db.Gender()})
    return HttpResponseRedirect('/pat/login')

def logout(request):
    del request.session['uid']
    del request.session['pwd']
    return HttpResponseRedirect('/pat/login')
