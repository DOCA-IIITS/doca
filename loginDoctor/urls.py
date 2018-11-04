from django.urls import path
from . import views
urlpatterns=[
    path('loginDoc/',views.index,name='index'),
    path('regDoc/',views.regDoc,name='Register_Patient'),
    path('verfDoc',views.verf,name='Verification'),
    path('forgotDoc',views.forgot,name='Forgot_Password'),
    path('forgotDoc/',views.forgot,name='Forgot_Password'),
    path('homeDoc/',views.home,name='Home'),
    path('udpDoc/',views.udp,name='udp'),
]
