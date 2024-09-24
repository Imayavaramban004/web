from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your models here.
def home(request):
    return render(request,'home.html',{'name':'magha akash'})
def add(request):
    res=int(request.POST.get('input1'))+int(request.POST.get('input2'))
    return render(request,'result.html',{'res':res})


