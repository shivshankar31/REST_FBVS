from mmap import PAGESIZE
from django.shortcuts import render
from rest_framework import views
from cbvapp.models import Employees
from cbvapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class EmpPagination(PageNumberPagination):
    page_size = 1

class EmployeeList(views.APIView):

    pagination_class = EmpPagination

    def get (self,request):
        emp = Employees.objects.all()
        empseri = EmployeeSerializer(emp, many = True)
        return Response(empseri.data)

    def post(self,request):
        empseri = EmployeeSerializer(data = request.data)
        if empseri.is_valid():
            empseri.save()
            return Response(empseri.data, status = status.HTTP_200_OK)
        return Response(empseri.error, status=status.HTTP_400_BAD_REQUEST)

        
class EmployeesDetails(views.APIView):

    pagination_class = EmpPagination

    def get_object(self,pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404
    
    def get(self,request,pk): 
        emp = self.get_object(pk)
        empdetail = EmployeeSerializer(emp) 
        return Response(empdetail.data)

    def put(self, request, pk):
        emp = self.get_object(pk)
        empupdate = EmployeeSerializer(emp, data=request.data)
        if empupdate.is_valid():
            empupdate.save()
            return Response(empupdate.data, status = status.HTTP_200_OK)
        return Response(empupdate.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emp = self.get_object(pk)
        emp.delete()
        return Response("Delete Successfull", status = status.HTTP_204_NO_CONTENT)




