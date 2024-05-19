from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(Investor)
admin.site.register(CarModel)
admin.site.register(Vehicle)