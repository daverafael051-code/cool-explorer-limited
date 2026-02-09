from django.db import models
from vehicles.models import Vehicle
from routes.models import Route
from drivers_app.models import Driver

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    trip_date = models.DateField()
    revenue_collected = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle} - {self.trip_date}"
