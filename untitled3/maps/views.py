from django.shortcuts import render
from django.http import  HttpResponse
from geopy.geocoders import Nominatim

# Create your views here.
def index(request):
    geolocator = Nominatim()
    request.session['user_loc']="hyderabad"
    location = geolocator.geocode(request.session['user_loc'])
    location.address
    a, b = (location.latitude, location.longitude)
    #return HttpResponse(b)

   # print(a, b)
    return render(request, 'maps/index.html',{'loc1': a , 'loc2': b})
def route(request,loc):
    return render(request, 'maps/routes.html',{'loc':loc,'user_location':request.session['user_loc']})
# def home(request):
#     return render(request,'home.html')
# def home2(request):
#     return render(request,'maps/home2.html')
# def home3(request):
#     return render(request,'maps/home3.html')
# def doca(request):
#     return render(request,'maps/doca.html')