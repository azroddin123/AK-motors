from django.db import models
from ak_admin.models import Vehicle
# Create your models here.


class ExpenseType(models.Model):
    expense_name = models.CharField(max_length=256,null=True,blank=True)


class Expense(models.Model):
    vehicle_name         = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True,blank=True)
    vehicle_no           = models.CharField(max_length=256,blank=True,null=True)
    expense_name         = models.ForeignKey(ExpenseType,on_delete=models.CASCADE,null=True,blank=True)
    expense_amount       = models.PositiveIntegerField(default=0)
    expense_image        = models.ImageField(upload_to="expense/",null=True,blank=True)
    notes                = models.TextField(null=True,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.vehicle_name:
            self.vehicle_name.recalculate_total_amount()

