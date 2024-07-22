from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from rest_framework.views import APIView
from portals.GM2 import GenericMethodsMixin
from rest_framework.response import Response
from rest_framework import status



class ExpenseTypeApi(GenericMethodsMixin,APIView):
    model = ExpenseType
    serializer_class = ETSerializer
    lookup_field = "id"


class ExpenseApi(GenericMethodsMixin,APIView):
    model = Expense
    serializer_class = ExpenseSerializer
    lookup_field = "id"
    def post(self,request,*args,**kwargs):
        try : 
            request.POST._mutable = True
            vehicle = request.data.get('vehicle_name')
            request.data['vehicle_no'] = int(vehicle)
            serializer = ExpenseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"error" : False,"data" : serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True,"message" : str(e)})


