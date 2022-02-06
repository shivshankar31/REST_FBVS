from django.shortcuts import render
from rest_framework import views
from cbvapp.models import Employees
from cbvapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Employeelist(views.APIView):

    def get (self,request):
        emp = Employees.object.all()
        empseri = EmployeeSerializer(emp, many = True)
        return Response(empseri.data)

    def post(self,request):
        empseri = EmployeeSerializer(data = request.data)
        if empseri.is_valid():
            empseri.save()
            return Response(empseri.data, status = status.HTTP_200_OK)
        return Response(empseri.error, status=status.HTTP_400_BAD_REQUEST)

        




