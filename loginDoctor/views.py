from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from loginDoctor.models import Doctor,DoctorApplied,DoctorF
from .form import loginDocForm,regDocForm,verfDocForm,forgotDocForm1,forgotDocForm2
from login2.views2 import send_otp,send_otp2
import random,datetime
from .form import udpDocForm
import os
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from django.conf import settings
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = loginDocForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            uidc=form.cleaned_data['uid'].lower()
            if Doctor.objects.filter(uid=uidc).count()==1:
                a=Doctor.objects.get(uid=uidc)
                if form.cleaned_data['password']==a.password:
                    request.session['uid']=uidc;
                    request.session['pwd']=a.password
                    return HttpResponseRedirect('/loginDoc/homeDoc/')
                else:

                    return render(request, 'loginDoc/index.html', {'form': form,'err':'Incorrect password !!!!!!!!!!!!'})
            else:

                return render(request, 'loginDoc/index.html', {'form': form,'err':'Incorrect Doctor id !!!!!!!!!!!!'})
    # if a GET (or any other method) we'll create a blank form
    else:
        if 'uid' in request.session:
            if 'pwd' in request.session:
                if Doctor.objects.filter(uid=request.session['uid']).count()==1:
                    a=Doctor.objects.get(uid=request.session['uid'])
                    if request.session['pwd']==a.password:
                        return HttpResponseRedirect('/loginDoc/homeDoc/')
        form = loginDocForm()

    return render(request, 'loginDoc/index.html', {'form': form})
def regDoc(request):
    if request.method == 'POST':
        form=regDocForm(request.POST)

        if form.is_valid():
            if Doctor.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                return render(request, 'loginDoc/register.html',{'form':form,'err':'email id is aleready in use !!!!!!'})
            otp_gen=random.randint(100000,999999)
            a=DoctorApplied(fname=form.cleaned_data['fn'],lname=form.cleaned_data['ln'],uid=form.cleaned_data['uid'].lower(),dob=form.cleaned_data['dob'],
            password=form.cleaned_data['password'],otp=otp_gen,gender=form.cleaned_data['gender'],city=form.cleaned_data['city'],
            address=form.cleaned_data['address'],state=form.cleaned_data['state'],country=form.cleaned_data['country']
            )
            a.save()
            send_otp(form.cleaned_data['uid'],otp_gen)
            return HttpResponseRedirect('/loginDoc/verfDoc?uidc='+form.cleaned_data['uid'])

        else:
            return render(request,'loginDoc/register.html',{'form':form})

    form=regDocForm()
    return render(request,'loginDoc/register.html',{'form':form})

def verf(request):
    if request.method == 'GET':
        uidc=request.GET.get('uidc','')
        if DoctorApplied.objects.filter(uid=uidc.lower()).count()==1:
            a=DoctorApplied.objects.get(uid=uidc.lower())
            b=a.otp
            if request.GET.get('otp','') == str(b) :
                b=Doctor(fname=a.fname,lname=a.lname,uid=a.uid,dob=a.dob,password=a.password,
                gender=a.gender,city=a.city,address=a.address,state=a.state,country=a.country)
                b.save()
                request.session['uid']=uidc.lower()
                request.session['pwd']=a.password
                a.delete()
                return HttpResponseRedirect('/loginDoc/udpDoc/')
            else:
                if request.GET.get('otp',''):
                    form=verfDocForm()
                    return render(request,'loginDoc/verf.html',{'form':form,'uidc':uidc,'err':'Invalid otp !!!!!'})
        else:
            form=verfDocForm()
            return render(request,'loginDoc/verf.html',{'form':form,'uidc':uidc,'err':'something went wrong !!!!!!!'})

    form=verfDocForm()
    uidc=request.GET.get('uidc','')
    return render(request,'loginDoc/verf.html',{'form':form,'uidc':uidc})

def forgot(request):
    if request.method=='GET':
        form=forgotDocForm1(request.GET)
        print('pass0')
        if form.is_valid():
            print(form.cleaned_data['uid'])
            if Doctor.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                a=Doctor.objects.get(uid=form.cleaned_data['uid'].lower())
                print('pass1')
                otp_gen=random.randint(100000,999999)
                if DoctorF.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                    print('pass1')
                    b=DoctorF.objects.get(uid=form.cleaned_data['uid'].lower())
                    b.delete()
                d=DoctorF(uid=form.cleaned_data['uid'].lower(),otp=otp_gen)
                d.save()
                send_otp2(form.cleaned_data['uid'],otp_gen)
                return render(request,'loginDoc/forgot.html',{'divn':'c4.css','uidc':form.cleaned_data['uid']})
            else :
                return render(request,'loginDoc/forgot.html',{'form':form,'divn':'c5.css','err':' no such account exists !!!!!!!'})
        else:
            return render(request,'loginDoc/forgot.html',{'form':form,'divn':'c5.css'})
    if request.method=='POST':
        form=forgotDocForm2(request.POST)
        uidc=request.POST.get('uid','').lower()
        if form.is_valid():
            if DoctorF.objects.filter(uid=uidc).count()==1:
                b=DoctorF.objects.get(uid=uidc)
                otp=b.otp
                if form.cleaned_data['otp']==str(otp):
                    a=Doctor.objects.get(uid=uidc)
                    a.password=form.cleaned_data['password']
                    a.save()
                    b.delete()
                    request.session['uid']=uidc;
                    request.session['pwd']=a.password
                    return HttpResponseRedirect('/loginDoc/homeDoc/')
                else:
                    print('p4')
                    return render(request,'loginDoc/forgot.html',{'form':form,'divn':'c4.css','err':'Incorrect otp  !!!!!!!','uidc':uidc})

    return render(request,'loginDoc/forgot.html',{'divn':'c4.css'})
from django.core.files.storage import default_storage
def udp(request):
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
        return HttpResponseRedirect('/loginDoc/loginDoc/')


    elif ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count()==1:
            a=Doctor.objects.get(uid=request.session['uid'])
            if request.session['pwd']==a.password:
                form = udpDocForm()
                return render(request, 'loginDoc/udp.html', {'form': form})

def home(request):
    if request.method=='POST':
        del request.session['uid']
        del request.session['pwd']
        return HttpResponseRedirect('/loginDoc/loginDoc/')
    elif ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count()==1:
            a=Doctor.objects.get(uid=request.session['uid'])
            if request.session['pwd']==a.password:

                return render(request,'loginDoc/home.html',{'uname':a.full_name,'udp':a.dp[7::]})

    return HttpResponseRedirect('/loginDoc/loginDoc/')













#
