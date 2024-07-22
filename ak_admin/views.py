from .serializers import *
from .models import *
from rest_framework.views import APIView
from portals.GM2 import GenericMethodsMixin
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User


class DashboardAPi(APIView):
    def get(self,request,*args,**kwargs):
        try : 
            total_investor = Investor.objects.count()        
            sold_vehicles_count = Vehicle.objects.filter(status="Sold").count() 
            total_amount = Vehicle.objects.aggregate(total=Sum('total_amount'))
            total_maintenance_amount = Vehicle.objects.aggregate(total=Sum('maintenance_cost'))
            total_employee = User.objects.filter(user_type="Employee").count() 
            data = {
                'total_investor': total_investor,
                'sold_vehicles_count': sold_vehicles_count,
                'total_amount': total_amount,
                'total_maintenance_amount': total_maintenance_amount,
                'total_employee': total_employee,
            }
            return Response({"error" : False,"data" : data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True,"message" : str(e)})
    
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
            request.POST._mutable = True
            investor = request.data.get('investor')
            request.data['investor'] = int(investor)
            request.data['brand_name']= int(request.data.get('investor'))
            serializer = VehicleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            vehicle = serializer.save()
            investor_obj = Investor.objects.get(id=investor)
            investor_obj.investment_amount = investor_obj.base_amount-vehicle.base_amount
            investor_obj.save()
            return Response({"error" : False,"data" : serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True,"message" : str(e)})
        
class EntryApi(GenericMethodsMixin,APIView):
    model  = Entry
    serializer_class = EntrySerializer
    lookup_field = "id"

class RTOPendingApi(GenericMethodsMixin,APIView):
    model = Vehicle
    serializer_class = VehicleSerializer
    lookup_field  = "id"
    
    def get(self, request, pk=None, *args, **kwargs):
        try:
            if pk is None or pk == 0: 
                vehicles = Vehicle.objects.filter(rto_status=False)
                serializer = VehicleSerializer(vehicles, many=True)
                return Response({"error": False, "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                vehicle = Vehicle.objects.get(id=pk)
                serializer = VehicleSerializer(vehicle)
                return Response({"error": False, "data": serializer.data}, status=status.HTTP_200_OK)
        except Vehicle.DoesNotExist:
            return Response({"error": True, "message": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": True, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
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