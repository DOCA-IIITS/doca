from django.conf.urls import url
from . import views

urlpatterns=[
        url(r'^book_appointments/',views.book,name='book'),
        url(r'^show_appointments/',views.showapp,name='showapp'),
        url(r'^yourappointments/',views.showappmnts,name='showappmnts'),
        url(r'^booked/',views.bookapp,name='bookapp'),
        url(r'^$',views.index,name='index'),


]