from django.urls import path
from .views import * 


urlpatterns = [
    path('investor',InvestorApi.as_view()),
    path('investor/<str:pk>', InvestorApi.as_view()),
    
    path('car-model',CarApi.as_view()),
    path('car-model/<str:pk>', CarApi.as_view()),
    
    path('vehicle',VehicleApi.as_view()),
    path('vehicle/<str:pk>', CarApi.as_view()),
    
]
