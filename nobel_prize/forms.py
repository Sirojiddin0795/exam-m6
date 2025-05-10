from django import forms
from .models import NobelPrize

class NobelPrizeForm(forms.ModelForm):
    class Meta:
        model = NobelPrize
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4})
        }