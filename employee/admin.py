from django.contrib import admin
from .models import * 
admin.site.register(ExpenseType)
admin.site.register(Expense)