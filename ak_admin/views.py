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
        
        
        
from openpyxl import Workbook
from django.http import HttpResponse

class ExportToExcel(APIView):
    def get(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.all()

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=vehicle_data.xlsx'

        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = 'Vehicles'

        # Header row
        headers = [
            'Brand Name', 'Model Name', 'Purchase Date', 'Purchase From',
            'Base Amount', 'Total Amount', 'Investor', 'Vehicle Type',
            'Maintenance Cost', 'Status', 'RTO Status', 'Sold Amount',
            'Sold Date', 'Notes'
        ]
        worksheet.append(headers)

        # Data rows
        for vehicle in vehicles:
            row = [
                vehicle.brand_name.brand_name if vehicle.brand_name else None,
                vehicle.model_name,
                vehicle.purchase_date if vehicle.purchase_date else '',
                vehicle.purchase_from,
                vehicle.base_amount,
                vehicle.total_amount,
                vehicle.investor.investor_name if vehicle.investor else None,
                vehicle.vehicle_type,
                vehicle.maintenance_cost,
                vehicle.status,
                'Yes' if vehicle.rto_status else 'No',
                vehicle.sold_amount if vehicle.sold_amount else '',
                vehicle.sold_date if vehicle.sold_date else '',
                vehicle.notes
            ]
            worksheet.append(row)

        workbook.save(response)
        return response