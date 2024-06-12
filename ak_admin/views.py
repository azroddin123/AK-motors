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

    def post(self,request,*args,**kwargs):
        try : 
            data = request.data
            investor = request.data.get('investor')
            serializer = VehicleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            vehicle = serializer.save()
            investor_obj = Investor.objects.get(id=investor)
            investor_obj.investment_amount = investor_obj.base_amount-vehicle.base_amount
            investor_obj.save()
            return Response({"error" : False,"data" : serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True,"message" : str(e)})

