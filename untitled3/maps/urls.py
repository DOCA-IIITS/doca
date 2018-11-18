from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('routes/<loc>/',views.route,name='routes'),

#     path('home',views.home,name="home"),
#     path('home2',views.home2,name="home2"),
#     path('home3',views.home3,name="home3"),
#     path('doca',views.doca,name="doca")
]