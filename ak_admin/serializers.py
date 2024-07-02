from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers
from django.db import models


class InvestorSerializer(ModelSerializer):
    class Meta :
        model = Investor
        fields = "__all__"

class CarSerializer(ModelSerializer):
    class Meta :
        model = CarModel
        fields = "__all__"

class VehicleSerializer(ModelSerializer):
    class Meta :
        model = Vehicle
        fields = "__all__"