from django.db import models
from django.db.models import Sum

class Investor(models.Model):
    investor_name     = models.CharField(max_length=256)
    investment_amount = models.IntegerField(default=0) 
    base_amount       = models.IntegerField(default=0)
    investor_pic      = models.ImageField(upload_to="investor/",null=True,blank=True)
    investment_date   = models.DateField(blank=True,null=True)
    returned_amount   = models.PositiveIntegerField(default=0)
    return_date       = models.DateField(blank=True,null=True)
    remarks           = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.investor_name
    
    def save(self, *args, **kwargs):
        # Check if the instance is being updated (not created) and if the returned_amount has changed
        if self.pk is not None:
            old_instance = Investor.objects.get(pk=self.pk)
            if old_instance.returned_amount != self.returned_amount:
                difference = self.returned_amount - old_instance.returned_amount
                self.base_amount -= difference
        super().save(*args, **kwargs)


class CarModel(models.Model):
    brand_name  = models.CharField(max_length=256)
    
    def __str__(self):
        return self.brand_name
    
# Create your models here.
class Vehicle(models.Model):
    brand_name       = models.ForeignKey(CarModel,on_delete=models.CASCADE,null=True,blank=True)
    model_name       = models.CharField(max_length=258)
    vehicle_pic      = models.ImageField(upload_to="vehicle/",null=True,blank=True)
    pic2             = models.ImageField(upload_to="vehicle/",null=True,blank=True)
    pic3             = models.ImageField(upload_to="vehicle/",null=True,blank=True)
   
    purchase_date    = models.DateField(blank=True,null=True)
    purchase_from    = models.CharField(max_length=258) 
    base_amount      = models.PositiveIntegerField(default=0)
    total_amount     = models.PositiveIntegerField(default=0)
    investor         = models.ForeignKey(Investor,on_delete=models.CASCADE,null=True,blank=True)
    
    vehicle_type     = models.CharField(max_length=258)
    maintenance_cost = models.PositiveIntegerField(default=0)
    status           = models.CharField(max_length=250,null=True,blank=True)
    rto_status       = models.BooleanField(default=False)
    sold_amount      = models.CharField(max_length=250,blank=True,null=True)
    sold_date        = models.DateField(blank=True,null=True)
    notes            = models.TextField(blank=True,null=True)

  
    
    def recalculate_total_amount(self):
        expenses_total = self.expense_set.aggregate(Sum('expense_amount'))['expense_amount__sum'] or 0
        self.total_amount = self.base_amount + expenses_total
        self.save(update_fields=['total_amount'])
    

