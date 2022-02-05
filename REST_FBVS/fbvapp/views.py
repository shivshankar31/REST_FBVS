from django.shortcuts import render
from fbvapp.models import Students
from fbvapp.serializers import StudentSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view




# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student = Students.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request,pk):
    try:
        stud = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(stud)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(stud,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
