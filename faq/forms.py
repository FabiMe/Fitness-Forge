from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }