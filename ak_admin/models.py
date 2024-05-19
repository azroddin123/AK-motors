from django.db import models



class Investor(models.Model):
    investor_name = models.CharField(max_length=256)

class CarModel(models.Model):
    model_name  = models.CharField(max_length=256)
    
# Create your models here.
class Vehicle(models.Model):
    vehicle_pic      = models.ImageField(null=True,blank=True)
    vehicle_type     = models.CharField(max_length=258)
    model_name       = models.CharField(max_length=258)
    purchase_date    = models.DateField()
    model_name       = models.CharField(max_length=258)
    vehicle_type     = models.CharField(max_length=258)
    model_name       = models.ForeignKey(CarModel,on_delete=models.CASCADE,null=True,blank=True)
    purchase_from    = models.CharField(max_length=258) 
    amount           = models.CharField(max_length=250)
    maintenance_cost = models.PositiveIntegerField(default=0)
    investor         = models.ForeignKey(Investor,on_delete=models.CASCADE,null=True,blank=True)
    notes            = models.TextField()



