from django.shortcuts import render
from django.http import HttpResponse

#Create your views here

def index(request):
    my_dict={'pranav':"This is from the template tagging!! Understand the concept?"}
    return render(request,'index.html',context=my_dict)
