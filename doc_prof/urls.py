from django.conf.urls import url
from . import views

app_name='doc_prof'

urlpatterns=[
    url('home/',views.home,name='home'),
    url('prof/',views.profile,name='profile'),
    url('login/',views.login,name='login'),
    url('register/',views.register,name='register'),
    url('logout/',views.logout,name='logout'),
    url('verf/',views.verf,name='verf'),
    url('udp/',views.udp,name='udp'),
]
