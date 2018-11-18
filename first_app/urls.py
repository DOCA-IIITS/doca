from django.conf.urls import url
from first_app import views

urlpatterns=[
        url(r'^book_appointments/',views.book,name='book'),
        url(r'^show_appointments/',views.showapp,name='showapp'),
        url(r'^booked/',views.bookapp,name='bookapp'),
        url(r'^$',views.index,name='index'),


]