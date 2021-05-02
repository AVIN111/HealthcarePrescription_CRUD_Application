from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['firstname','lastname','Address','age','gender','department','precondition','allergic','height','profile']
        widgets = {
            'gender': forms.RadioSelect(),
            'department': forms.RadioSelect(),
            'Address': forms.Textarea()
           }
        
    

 