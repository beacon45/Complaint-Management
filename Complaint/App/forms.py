from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'phone', 'complaintText', 'uploadFile', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
