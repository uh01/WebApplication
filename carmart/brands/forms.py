from django import forms
from .models import BrandsModel

class BrandsForm(forms.ModelForm):
    class Meta:
        model = BrandsModel
        fields = ['brandName']
        # fields = '__all__'