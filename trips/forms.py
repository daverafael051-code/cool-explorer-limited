from django import forms
from .models import Trip
from drivers_app.models import Driver

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['vehicle', 'route', 'driver', 'trip_date', 'revenue_collected']
        widgets = {
            'trip_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show only ACTIVE drivers
        self.fields['driver'].queryset = Driver.objects.filter(status='Active')
