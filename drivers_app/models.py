from django.db import models

class Driver(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    id_number = models.CharField(max_length=20, unique=True)
    license_number = models.CharField(max_length=50, unique=True)

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    date_hired = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
