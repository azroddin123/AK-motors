from django.urls import path
from .views import * 


urlpatterns = [
    path('expense-type',ExpenseTypeApi.as_view()),
    path('expense-type/<int:pk>', ExpenseTypeApi.as_view()),

    path('expense',ExpenseApi.as_view()),
    path('expense/<int:pk>', ExpenseApi.as_view()),
]