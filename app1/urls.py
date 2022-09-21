from django.urls import path
from . import views

urlpatterns=[
    path('myindex1/',views.fun1,name="index"),
    path('myhome/',views.fun2,name="home"),
    
]