from django.shortcuts import render
from login2.models import user
from django.http import HttpResponseRedirect,HttpResponse
from loginDoctor.models import Doctor
from .models import msg
from .models import msg as m
from .form import msgForm
from django.db.models import Q
import os
from django.conf import settings
from django.core.files.storage import default_storage
def con(request):

    if request.method=='POST':
        request.session['rec']=request.POST.get('rec','')
        return HttpResponseRedirect('/chat/chat/')
    msg_list=[]
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            a=user.objects.filter(uid=request.session['uid']).values()
            dir_path = os.getcwd()
            for udp in a:
                try:
                    f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                    f.close()
                except FileNotFoundError:
                    udp['dp']='static1/uploads/A@DOCA@IIIT@DPdefualt.png'
            b=m.objects.filter(Q(suid=request.session['uid'])|Q(ruid=request.session['uid'])).values_list('suid','ruid').distinct()
            for i in b:
                if i[0]==request.session['uid']:
                    msg_list.append(i[1])
                else:
                    msg_list.append(i[0])
            msg_list=list(set(msg_list))
            c=Doctor.objects.filter(uid__in=msg_list).values_list('uid','fname','dp')
            d=[]
            for xdp in c:

                xdp=list(xdp)
                try:
                    f=open(dir_path+'/'+xdp[2][:14]+'/'+xdp[2][16:])
                    f.close()
                except FileNotFoundError:
                    xdp[2]='static/uploads\/A@DOCA@IIIT@DPdefualt.png'
                d.append(xdp)
            return render(request,'Chatbox/ChatContant.html',{'user_data':a,'doctor_list':d})


        elif Doctor.objects.filter(uid=request.session['uid']).count()==1:
            a=Doctor.objects.filter(uid=request.session['uid']).values()
            dir_path = os.getcwd()
            for udp in a:
                try:
                    f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                    f.close()
                except FileNotFoundError:
                    udp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'
            b=m.objects.filter(Q(suid=request.session['uid'
            ])|Q(ruid=request.session['uid'])).values_list('suid','ruid').distinct()
            for i in b:
                if i[0]==request.session['uid']:
                    msg_list.append(i[1])
                else:
                    msg_list.append(i[0])
            msg_list=list(set(msg_list))
            c=user.objects.filter(uid__in=msg_list).values_list('uid','fname','dp')
            d=[]
            for xdp in c:
                print(xdp)
                xdp=list(xdp)
                print('\n\n\npass1\n\n')
                try:
                    print('\n\n\npass2\n\n')
                    f=open(dir_path+'/'+xdp[2][:14]+'/'+xdp[2][16:])
                    print("aibale")
                    f.close()
                except FileNotFoundError:
                    xdp[2]='static/uploads/A@DOCA@IIIT@DPdefualt.png'
                d.append(xdp)
            print(c)
            return render(request,'Chatbox/ChatContant.html',{'user_data':a,'doctor_list':d,'sid':request.session.session_key})


        else:
            del request.session['pwd']
            del request.session['uid']
            return  HttpResponseRedirect('/login/login/')
    return  HttpResponseRedirect('/login/login/')

def chat(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            if 'rec' in request.session:
                if Doctor.objects.filter(uid=request.session['rec']).count()==1:
                    a=Doctor.objects.filter(uid=request.session['rec']).values()

                    dir_path = os.getcwd()
                    for udp in a:
                        try:
                            f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                            f.close()

                        except FileNotFoundError:
                            udp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'
                    if request.method=='POST':
                        form=msgForm(request.POST)
                        if form.is_valid():
                            if (form.cleaned_data['msg'] is not None) | (form.cleaned_data['img'] is not None):
                                msg_data=m(suid=request.session['uid'],ruid=request.session['rec'],msg=form.cleaned_data['msg'])
                                msg_data.save()
                                if len(request.POST.get('img','Avi')) !=0:

                                    save_path = os.path.join(settings.MEDIA_ROOT, 'static/uploads',request.POST.get('img',''))
                                    path = default_storage.save(save_path, request.FILES['img'])
                                    save_path=save_path+'/'+str(msg_data.id)+'.png'
                                    msg_data.imgmsg=save_path;
                                    msg_data.save()
                                    try:
                                        os.rename(path,save_path)
                                    except FileExistsError:
                                        os.remove(save_path)
                                        os.rename(path,save_path)
                                elif form.cleaned_data['msg']=='':
                                    msg_data.delete()


                    form=msgForm()
                    return render(request,'Chatbox/chat.html',{'user_data':a,'form':form})
                else:
                    del request.session['rec']
            return HttpResponseRedirect('/chat/chatbox/')
        elif Doctor.objects.filter(uid=request.session['uid']).count()==1:
            if 'rec' in request.session:
                if user.objects.filter(uid=request.session['rec']).count()==1:

                    a=user.objects.filter(uid=request.session['rec']).values()
                    dir_path = os.getcwd()
                    for udp in a:
                        try:
                            f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                            f.close()
                        except FileNotFoundError:
                            udp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'
                    if request.method=='POST':
                        form=msgForm(request.POST)
                        if form.is_valid():
                            if (form.cleaned_data['msg'] is not None) | (form.cleaned_data['img'] is not None):
                                msg_data=m(suid=request.session['uid'],ruid=request.session['rec'],msg=form.cleaned_data['msg'])
                                msg_data.save()
                                if len(request.POST.get('img','Avi')) !=0:
                                    print(form.cleaned_data['img'])

                                    save_path = os.path.join(settings.MEDIA_ROOT, 'static/uploads',request.POST.get('img',''))
                                    path = default_storage.save(save_path, request.FILES['img'])

                                    save_path=save_path+'/'+str(msg_data.id)+'.png'
                                    msg_data.imgmsg=save_path;
                                    msg_data.save()
                                    try:
                                        os.rename(path,save_path)
                                    except FileExistsError:
                                        os.remove(save_path)
                                        os.rename(path,save_path)
                                elif form.cleaned_data['msg']=='':
                                    msg_data.delete()




                    form=msgForm()
                    return render(request,'Chatbox/chat.html',{'user_data':a,'form':form})
                else:
                    del request.method['rec']
            return HttpResponseRedirect('/chat/chatbox/')
    return HttpResponseRedirect('/login/login/')

def msg(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            if 'rec' in request.session:
                a=m.objects.filter(Q(Q(suid=request.session['uid']) & Q(ruid=request.session['rec']))|Q(ruid=request.session['uid'])& Q(suid=request.session['rec'])).values('suid','ruid','msg','imgmsg','msgtime').order_by('-msgtime')
                return render(request,'Chatbox/msg.html',{'msg_list':a,'uid':request.session['uid']})
            else:
                del request.method['rec']
            return HttpResponseRedirect('/chat/chatbox/')
        if Doctor.objects.filter(uid=request.session['uid']).count()==1:
            if 'rec' in request.session:
                a=m.objects.filter(Q(Q(suid=request.session['uid']) & Q(ruid=request.session['rec']))|Q(ruid=request.session['uid'])& Q(suid=request.session['rec'])).values('suid','ruid','msg','imgmsg','msgtime').order_by('-msgtime')
                return render(request,'Chatbox/msg.html',{'msg_list':a,'uid':request.session['uid']})
            else:
                del request.method['rec']
            return HttpResponseRedirect('/chat/chatbox/')
    return HttpResponseRedirect('/login/login/')

def adnew(request):

    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            if request.method=='POST':
                request.session['rec']=request.POST.get('rec','')
                return HttpResponseRedirect('/chat/chat/')
            if request.method=='GET':
                if 'usearch' in request.GET:
                #print(request.GET.get('usearch'))
                    if request.GET.get('usearch')!='':
                        b=Doctor.objects.filter(fname__icontains=request.GET.get('usearch')).values('fname','dp','uid')[:10]

                        dir_path = os.getcwd()
                        for udp in b:
                            try:
                                f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                                f.close()
                            except FileNotFoundError:
                                xdp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'

                        return render(request,'Chatbox/search.html',{'User':b})

    return render(request,'Chatbox/search.html',{'b':10})

def call(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if user.objects.filter(uid=request.session['uid']).count()==1:
            a=Doctor.objects.filter(uid=request.session['rec']).values()
            dir_path = os.getcwd()
            for udp in a:
                try:
                    f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                    f.close()
                except FileNotFoundError:
                    udp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'

            return render(request,'Chatbox/call.html',{'dp':a[0],'me':request.session['uid']})
        elif Doctor.objects.filter(uid=request.session['uid']).count()==1:
            a=user.objects.filter(uid=request.session['rec']).values()
            dir_path = os.getcwd()
            for udp in a:
                try:
                    f=open(dir_path+'/'+udp['dp'][:14]+'/'+udp['dp'][16:])
                    f.close()
                except FileNotFoundError:
                    udp['dp']='static/uploads/A@DOCA@IIIT@DPdefualt.png'

            return render(request,'Chatbox/call.html',{'dp':a[0],'me':request.session['uid']})
    return HttpResponseRedirect('/login/login/')


def vchat(request):
    return render(request,'Chatbox/videoCall.html')








# Create your views her
