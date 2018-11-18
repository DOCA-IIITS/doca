from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models2 import file_save as fs
from login2.models import user
from loginDoctor.models import Doctor

def file_save(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            if 'rec' in request.session:
                if Doctor.objects.filter(uid=request.session['rec']).count()==1:
                    a=Doctor.objects.filter(uid=request.session['rec']).values()
                    print(request.method)
                    if request.method=="POST":
                        print("on refresh")

                        a=fs(pid=request.session['uid'],did=request.session['rec'],file_path="abc")
                        a.save()
                        print("hello")
                    return render(request,'Chatbox/file_save.html')
                else:
                    del request.session['rec']
            return HttpResponseRedirect('/chat/chatbox/')
        elif Doctor.objects.filter(uid=request.session['uid']).count()==1:
            if 'rec' in request.session:
                if user.objects.filter(uid=request.session['rec']).count()==1:
                    a=user.objects.filter(uid=request.session['rec']).values()
                    return render(request,'Chatbox/file_save.html')

                else:
                    del request.method['rec']
            return HttpResponseRedirect('/chat/chatbox/')
    return HttpResponseRedirect('/login/login/')
