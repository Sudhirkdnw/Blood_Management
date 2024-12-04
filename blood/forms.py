from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','bloodgroup','unit']

class ReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = ['user', 'address', 'phone_number', 'sugar_level', 'medicine', 'other_details']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'sugar_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'medicine': forms.Textarea(attrs={'class': 'form-control'}),
            'other_details': forms.Textarea(attrs={'class': 'form-control'}),
        }
