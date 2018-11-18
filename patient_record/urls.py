from django.urls import path,include
from . import views

urlpatterns = [
    path('a',views.index,name = ''),
    path('form',views.user_form,name = ''),
    # path('report',views.repo,name = ''),
    path('search',views.search,name = ''),
    path('photos',views.photos,name = ''),
    path('history',views.history,name = ''),
    path('history_utils',views.history_util,name = ''),

]
