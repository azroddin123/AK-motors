from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *


class ETSerializer(ModelSerializer):
    class Meta :
        model = ExpenseType
        fields = "__all__"


class ExpenseSerializer(ModelSerializer):
    class Meta :
        model = Expense
        fields = "__all__"