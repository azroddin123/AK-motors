from django.urls import path
from .views import * 


urlpatterns = [
    path('investor',InvestorApi.as_view()),
    path('investor/<str:pk>', InvestorApi.as_view()),
    
    path('car-model',CarApi.as_view()),
    path('car-model/<str:pk>', CarApi.as_view()),
    
    path('vehicle',VehicleApi.as_view()),
    path('vehicle/<str:pk>', VehicleApi.as_view()),
    
    path('rto-pending',RTOPendingApi.as_view()),
    path('rto-pending/<str:pk>',RTOPendingApi.as_view()),
    
    
    path('entry',EntryApi.as_view()),
    path('entry/<str:pk>', EntryApi.as_view()),
    
    path('export-vehicles/', ExportToExcel.as_view(), name='export-vehicles'),
    
]
