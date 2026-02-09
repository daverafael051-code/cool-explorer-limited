from django.db import models

class Route(models.Model):
    route_name = models.CharField(max_length=50)
    start_point = models.CharField(max_length=50)
    end_point = models.CharField(max_length=50)
    distance_km = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.route_name
