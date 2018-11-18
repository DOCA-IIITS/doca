from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name="final_app"

urlpatterns = [
    #path('index/',views.index,name='index'),
    path('review/',views.review,name='review'),
    #path('calculate/',views.calculate,name='calculate'),

]
