from rest_framework import serializers
from .models import EmployeeTable

class EmployeeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model=EmployeeTable
        fields= '__all__'