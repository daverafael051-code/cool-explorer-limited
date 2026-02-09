from django.db import models

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField(help_text="Number of passengers")
    status = models.CharField(
        max_length=20,
        choices=[('Available', 'Available'), ('In Service', 'In Service'), ('Out of Service', 'Out of Service')],
        default='Available'
    )

    def __str__(self):
        return self.plate_number
