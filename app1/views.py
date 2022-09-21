from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def fun1(request):
    return HttpResponse("this is my first app")
def fun2(request):
    return render(request, 'home.html') 
