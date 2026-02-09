from django.db import models
from vehicles.models import Vehicle

class Expense(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"
