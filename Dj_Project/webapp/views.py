#from django.core.serializers import serialize
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from webapp.serialization import EmpSerializer
from webapp.models import Employee
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# Create your views here.
@api_view(['GET','POST'])
def read_data(request):
            if request.method == 'GET':
                emp = Employee.objects.all()
                serializer = EmpSerializer(emp, many = True)
                return Response(serializer.data)
            elif request.method == 'POST':
                   serializer = EmpSerializer(data=request.data)
                   if serializer.is_valid():
                        serializer.save()
                        return Response({'Message':'Data created successfully!!!'})
                   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except emp.DoesnotNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        #emp = Employee.objects.get(pk=pk)
        serializer = EmpSerializer(emp)
        return Response(serializer.data)
    elif request.method == 'PUT':
            #emp = Employee.objects.get(pk=pk)
            serializer = EmpSerializer(emp, data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        #emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response({'Message':'Data deleted successfully!!!'})






