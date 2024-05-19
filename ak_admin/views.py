from .serializers import *
from .models import *
from rest_framework.views import APIView
from portals.GM2 import GenericMethodsMixin
from rest_framework.response import Response
from rest_framework import status


class InvestorApi(GenericMethodsMixin,APIView):
    model = Investor
    serializer_class = InvestorSerializer
    lookup_field = "id"


class CarApi(GenericMethodsMixin,APIView):
    model = CarModel
    serializer_class = CarSerializer
    lookup_field = "id"

class VehicleApi(GenericMethodsMixin,APIView):
    model = Vehicle
    serializer_class = VehicleSerializer
    lookup_field = "id"