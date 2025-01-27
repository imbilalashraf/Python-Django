from django import forms
from cars.models import Car

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car  # Specify the model class
        fields = ['car_name', 'car_model', 'car_speed']  # Specify the fields to include
        widgets= {
            'car_name': forms.TextInput(attrs={'class': 'form-control'}),
            'car_model': forms.NumberInput(attrs={'class': 'form-control'}),
            'car_speed': forms.NumberInput(attrs={'class': 'form-control'}),
        }
