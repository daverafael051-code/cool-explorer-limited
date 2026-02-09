from django.db import models

class Member(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    payment_preference = models.CharField(
        max_length=20,
        choices=[('Bank', 'Bank'), ('Mpesa', 'Mpesa')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
