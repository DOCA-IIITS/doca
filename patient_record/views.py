from django.shortcuts import render
from django.http import    HttpResponse,HttpResponseRedirect  #object
from .models import patient_record
from loginDoctor.models import Doctor
from .forms import  UserForm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from django.db.models import Q
from ChatBox.models2 import file_save as fs
from Appointements.models import Appointments
from login2.models import user

def user_form(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count()==1:
            print("userform")
            form=UserForm()
            print(form)
            form_dict={'form':form}

            if request.method == 'POST':
                form=UserForm(request.POST) #passing request
                if form.is_valid():
                    print(request.session['pat_id'])
                    ddic=patient_record(did=Doctor.objects.get(uid=request.session["uid"]),pid=user.objects.get(uid=request.session["pat_id"]),comment=form.cleaned_data['comment'],disease=form.cleaned_data['disease'])  #ddic tuplea
                    ddic.save()
                    return render(request,'patient_record/form_page.html',form_dict)
                else:
                    print("invalid form")
            return render(request,'patient_record/form_page.html',form_dict)
        else:
            return HttpResponseRedirect('/login/login/')
    else:
        return HttpResponseRedirect('/loginDoc/loginDoc/')

def history_util(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count() == 1:
            if request.method == 'POST':
                a=request.POST.get('input','')
                request.session['pat_id']=a
                return HttpResponseRedirect('/patient/form')
        else:
            return HttpResponseRedirect('/login/login/')
    else:
        return HttpResponseRedirect('/loginDoc/loginDoc/')

def index(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count() == 1:
            print("index")

            request.session['patient_flag']=0   #flag for show medical records , initial value
            patient_ids=patient_record.objects.values('pid_id').distinct().order_by()[:10]

            print(patient_ids)
            #taken from patient_record module which stores those patient_id in which dr stored a comment
            A=[]
            for i in patient_ids:

                patient_names_dic={}
                uSer=user.objects.get(uid=i['pid_id'])
                patient_names_dic['name']=uSer.fname+" "+uSer.lname
                patient_names_dic['id']=i['pid_id']
                print(patient_names_dic['name'])
                A.append(patient_names_dic)


            my_dict={'insert_me' : 'hello i am from views.py' ,'patientname':A ,
            'diseases':patient_record.objects.values('disease').order_by('date').distinct()
            #pid_id is used because pid is a foreign key and pid returns address of object , we are dereferencing it
            }
            return render(request, 'patient_record/index.html', context=my_dict ) # report page for doctor
        else:
            return HttpResponseRedirect('/login/login/')
    else:
        return HttpResponseRedirect('/loginDoc/loginDoc/')


def history(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count() == 1:
            print("history")
            duid=request.session['uid']
            a=Appointments.objects.filter(doctor_id=duid).values('patient_id','date')[:10] #list
            A=[]
            for i in a:
                B={}
                B['patient_id']=i['patient_id']
                B['date']=i['date']
                uSer=user.objects.get(uid=i['patient_id'])   # returns one row bec of get fnc and ForeignKey used
                B['full_name']=uSer.fname+" "+uSer.lname
                B['dp']=uSer.dp   # gets the path of users profile pic
                A.append(B)
            context={
            "user":A,
            }
            return render(request,"patient_record/history.html",context=context)
        else:
            return HttpResponseRedirect('/login/login/')
    else:
        return HttpResponseRedirect('/loginDoc/loginDoc/')



def search(request):
    if ('uid' in request.session) & ('pwd' in request.session):
        if Doctor.objects.filter(uid=request.session['uid']).count() == 1:
            print("search")
            names=request.POST.get('patient_name')   #from select down menu for patient, returns 0if none ,else returns pid_id of selected patient
            print(names)
            diseases=request.POST.get('disease')
            request.session['patient_flag']=0   #flag for show medical records , initial value

            result=None
            if (names!='0' and diseases!='0' ):
                result = patient_record.objects.filter(Q(pid_id=names)&Q(disease=diseases)).values().order_by('date')

            elif (names!='0'):  # only patient selected from select down menu
                result = patient_record.objects.filter(pid_id=names ).values().order_by('date')
                request.session['patient_flag']=1   #flag for show medical records
                request.session['patient_selected']=names  #globalising which patient has been slected

            elif (diseases!='0') :
                result = patient_record.objects.filter(disease=diseases ).values().order_by('date')
            A=[]
            B={}
            C=[]
            if(result is not None):
                for i in result:   #for getting patient name from user table made by Avinash

                    B['pid_id']=i['pid_id']
                    B['date']=i['date']
                    B['comment']=i['comment']
                    B['disease']=i['disease']
                    uSer=user.objects.get(uid=i['pid_id'])   # returns one row bec of get fnc and ForeignKey used
                    B['full_name']=uSer.fname+" "+uSer.lname
                    B['dp']=uSer.dp   # gets the path of users profile pic
                    print(uSer.dp)
                    A.append(B)
            patient_ids=patient_record.objects.values('pid_id').distinct().order_by() #[:10]
                #taken from patient_record module which stores those patient_id in which dr stored a comment

            for i in patient_ids:     # for patientname in select menu ,to tackle request coming from views.search
                patient_names_dic={}  # independent from search function
                uSer=user.objects.get(uid=i['pid_id'])
                patient_names_dic['name']=uSer.fname+" "+uSer.lname
                patient_names_dic['id']=i['pid_id']
                print(patient_names_dic['name'])
                C.append(patient_names_dic)

            context={
                "results":A,
                'patientname':C,
                'diseases':patient_record.objects.values('disease').distinct().order_by('disease')[:100],}

            print(context['diseases'])
            return render(request,"patient_record/index.html",context=context)
        else:
            return HttpResponseRedirect('/login/login/')
    else:
        return HttpResponseRedirect('/loginDoc/loginDoc/')




def photos(request):
    if Doctor.objects.filter(uid=request.session['uid']).count() == 1:
        if ('uid' in request.session) & ('pwd' in request.session):
            print("photos")
            if request.method == 'POST':
                if(request.session['patient_flag']==1):   #flag for show medical records , initial value
                    context={"photos":fs.objects.filter(pid=request.session['patient_selected']).values('file_path')#[:10]
                    ,
                    'patientname':patient_record.objects.values('pid').distinct().order_by('pid')[:100],
                    'diseases':patient_record.objects.values('disease').distinct().order_by('disease')[:100],
                    }
                    context['count']=0
                    print(context)
                    return render(request,"patient_record/index2.html",context)
                return  HttpResponse("<h1>No record found</h1>")
        else:
            return HttpResponseRedirect('/login/login/')
    else:
        return HttpResponseRedirect('/loginDoc/loginDoc/')


# def repo(request):
#     fig = Figure()
#     canvas = FigureCanvas(fig)
#     ax = fig.add_subplot(111)
#     x = np.arange(-2,1.5,.01)
#     y = np.sin(np.exp(2*x))
#     ax.plot(x, y)
#     response=django.http.HttpResponse(content_type='image/png')
#     canvas.print_png(response)
#     return response
