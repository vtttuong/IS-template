from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'a':'HelloWorld'}
    return render(request,'matches.html',context=context)