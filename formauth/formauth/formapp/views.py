from django.shortcuts import render
from formapp import forms


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeTable
from .serializers import EmployeeTableSerializer

# Create your views here.


def index(request):
    return render(request, "formapp/index.html")


def form_function(request):
    form = forms.Employee()
    if request.method == "POST":
        form = forms.Employee(request.POST)

        if form.is_valid():
            print("Validation Successful")
            print("Name: " + form.cleaned_data["emp_name"])
            print("Email: " + form.cleaned_data["emp_email"])
            print("Comments: " + form.cleaned_data["comment"])

    return render(request, "formapp/form.html", {'form' : form})




class employeeList(APIView):
    def get(self, request):
        employees= EmployeeTable.objects.all()
        serializer= EmployeeTableSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
