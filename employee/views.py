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


