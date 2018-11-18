from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from login2.models import user,userApplied,userF
from .form import loginForm,regpatientForm,verfForm,forgotForm1,forgotForm2
from .views2 import send_otp,send_otp2
import random,datetime
from .form import udpForm
import os
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from django.conf import settings
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = loginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            uidc=form.cleaned_data['uid'].lower()
            if user.objects.filter(uid=uidc).count()==1:
                a=user.objects.get(uid=uidc)
                if form.cleaned_data['password']==a.password:
                    request.session['uid']=uidc;
                    request.session['pwd']=a.password
                    return HttpResponseRedirect('/login/home/')
                else:

                    return render(request, 'login2/index.html', {'form': form,'err':'Incorrect password !!!!!!!!!!!!'})
            else:

                return render(request, 'login2/index.html', {'form': form,'err':'Incorrect user id !!!!!!!!!!!!'})
    # if a GET (or any other method) we'll create a blank form
    else:
        if 'uid' in request.session:
            if 'pwd' in request.session:
                if user.objects.filter(uid=request.session['uid']).count()==1:
                    a=user.objects.get(uid=request.session['uid'])
                    if request.session['pwd']==a.password:
                        return HttpResponseRedirect('/login/home/')
        form = loginForm()

    return render(request, 'login2/index.html', {'form': form})
def regpatient(request):
    if request.method == 'POST':
        form=regpatientForm(request.POST)
        print(form)


        if form.is_valid():
            print(form)

            if user.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                return render(request, 'login2/register.html',{'form':form,'err':'email id is aleready in use !!!!!!'})
            otp_gen=random.randint(100000,999999)
            a=userApplied(fname=form.cleaned_data['fn'],lname=form.cleaned_data['ln'],uid=form.cleaned_data['uid'].lower(),dob=form.cleaned_data['dob'],
            password=form.cleaned_data['password'],otp=otp_gen,gender=form.cleaned_data['gender'],city=form.cleaned_data['city'],
            address=form.cleaned_data['address'],state=form.cleaned_data['state'],country=form.cleaned_data['country']
            )
            a.save()
            send_otp(form.cleaned_data['uid'],otp_gen)
            return HttpResponseRedirect('/login/verf?uidc='+form.cleaned_data['uid'])

        else:
            return render(request,'login2/register.html',{'form':form})

    form=regpatientForm()
    return render(request,'login2/register.html',{'form':form})

def verf(request):
    if request.method == 'GET':
        uidc=request.GET.get('uidc','')
        if userApplied.objects.filter(uid=uidc.lower()).count()==1:
            a=userApplied.objects.get(uid=uidc.lower())
            b=a.otp
            if request.GET.get('otp','') == str(b) :
                b=user(fname=a.fname,lname=a.lname,uid=a.uid,dob=a.dob,password=a.password,
                gender=a.gender,city=a.city,address=a.address,state=a.state,country=a.country)
                b.save()
                request.session['uid']=uidc.lower()
                request.session['pwd']=a.password
                a.delete()
                return HttpResponseRedirect('/login/udp/')
            else:
                if request.GET.get('otp',''):
                    form=verfForm()
                    return render(request,'login2/verf.html',{'form':form,'uidc':uidc,'err':'Invalid otp !!!!!'})
        else:
            form=verfForm()
            return render(request,'login2/verf.html',{'form':form,'uidc':uidc,'err':'something went wrong !!!!!!!'})

    form=verfForm()
    uidc=request.GET.get('uidc','')
    return render(request,'login2/verf.html',{'form':form,'uidc':uidc})

def forgot(request):
    if request.method=='GET':
        form=forgotForm1(request.GET)
        print('pass0')
        if form.is_valid():
            print(form.cleaned_data['uid'])
            if user.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                a=user.objects.get(uid=form.cleaned_data['uid'].lower())
                print('pass1')
                otp_gen=random.randint(100000,999999)
                if userF.objects.filter(uid=form.cleaned_data['uid'].lower()).count()==1:
                    print('pass1')
                    b=userF.objects.get(uid=form.cleaned_data['uid'].lower())
                    b.delete()
                d=userF(uid=form.cleaned_data['uid'].lower(),otp=otp_gen)
                d.save()
                send_otp2(form.cleaned_data['uid'],otp_gen)
                return render(request,'login2/forgot.html',{'divn':'c4.css','uidc':form.cleaned_data['uid']})
            else :
                return render(request,'login2/forgot.html',{'form':form,'divn':'c5.css','err':' no such account exists !!!!!!!'})
        else:
            return render(request,'login2/forgot.html',{'form':form,'divn':'c5.css'})
    if request.method=='POST':
        form=forgotForm2(request.POST)
        uidc=request.POST.get('uid','').lower()
        if form.is_valid():
            if userF.objects.filter(uid=uidc).count()==1:
                b=userF.objects.get(uid=uidc)
                otp=b.otp
                if form.cleaned_data['otp']==str(otp):
                    a=user.objects.get(uid=uidc)
                    a.password=form.cleaned_data['password']
                    a.save()
                    b.delete()
                    request.session['uid']=uidc;
                    request.session['pwd']=a.password
                    return HttpResponseRedirect('/login/home/')
                else:
                    print('p4')
                    return render(request,'login2/forgot.html',{'form':form,'divn':'c4.css','err':'Incorrect otp  !!!!!!!','uidc':uidc})

    return render(request,'login2/forgot.html',{'divn':'c4.css'})
from django.core.files.storage import default_storage
def udp(request):
    if request.method == 'POST':
        save_path = os.path.join(settings.MEDIA_ROOT, 'static/uploads',request.POST.get('file',''))
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
        return HttpResponseRedirect('/login/login/')


    elif ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            a=user.objects.get(uid=request.session['uid'])
            if request.session['pwd']==a.password:
                form = udpForm()
                return render(request, 'login2/udp.html', {'form': form})

def home(request):
    print(request.session)
    if request.method=='POST':
        del request.session['uid']
        del request.session['pwd']
        return HttpResponseRedirect('/login/login/')
    elif ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            a=user.objects.filter(uid=request.session['uid']).values()
            if request.session['pwd']==a[0]['password']:
                dir_path = os.getcwd()
                for udp in a:
                    try:
                        f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                        f.close()
                    except FileNotFoundError:
                        udp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'
                    except NotADirectoryError:
                        udp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'
                return render(request,'login2/home.html',{'uname':a[0]['fname']+" "+a[0]['lname'],'udp':a[0]['dp'][7::]})

    return HttpResponseRedirect('/login/login/')
def imgret(request,udp):
    return render(request,"login2/imgret.html",{'udp':udp})













#
