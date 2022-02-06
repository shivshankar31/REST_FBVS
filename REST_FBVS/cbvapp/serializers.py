from dataclasses import fields
from rest_framework import serializers
from cbvapp.models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['Id', 'Name', 'Salary', 'Department']

        