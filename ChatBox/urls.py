from django.urls import path
from . import views
urlpatterns=[
    path('chatbox/',views.con,name='index'),
    path('chat/',views.chat,name='index'),
    path('msg/',views.msg,name='index'),
    path('addnew/',views.adnew,name='index'),
    path('call/',views.call,name='call'),
    path('Vcall/',views.vchat,name='Vcall'),
]
