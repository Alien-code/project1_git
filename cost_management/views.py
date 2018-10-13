from django.shortcuts import render
from .models import Expense

# Create your views here.
def my_expense(request):
    expenses = Expense.objects.all()
    return render(request, 'cost/expense.html', {'expenses': expenses})

