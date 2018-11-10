from django.shortcuts import render
from django.http import HttpResponse
from .models import category,location,doctor
from .forms import FormName,AppForm


# Create your views here.
def index(request):


    return render(request, "first_app/homepage.html")

def book(request):
    form=FormName(request.POST)
    #if form.is_valid():
    #    loc=form.cleaned_data['loc']
    #    cat=form.cleaned_data['cat']
    #   details=doctor.objects.filter(location=loc)


        #print(loc)
        #print(cat)
    #print(form)
    context = {
        "categories": category.objects.all(),
        "locations": location.objects.all(),

    }



    return render(request, "first_app/book_appointments.html", context=context)

def showapp(request):

    loc=request.POST.get('loc')
    cat=request.POST.get('cat')
    details = doctor.objects.filter(location__loc_name=loc and category__cat_name=cat).values()
    context={
        "doctors":details,
    }


    return render(request,"first_app/show_appointments.html",context=context)

def bookapp(request):
    form=AppForm()
    #if request.method=="POST":
    #    form=AppForm(request.POST)
    #    if form.is_valid():
    #        form.save(commit=True)
    #    else:
    #        print("FORM INVALID")


    doc_name=request.POST.get('doc_name')
    fees=request.POST.get('fees')
    rating=request.POST.get('rating')
    #form.doc_name=doc_name
    #form.fees=fees
    #form.rating=rating
    #form.save()

    return render(request,"first_app/booked.html")