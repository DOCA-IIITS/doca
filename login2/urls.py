from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.index,name='index'),
    path('regpatient/',views.regpatient,name='Register_Patient'),
    path('verf',views.verf,name='Verification'),
    path('forgot',views.forgot,name='Forgot_Password'),
    path('forgot/',views.forgot,name='Forgot_Password'),
    path('home/',views.home,name='Home'),
    path('udp/',views.udp,name='udp'),
]
