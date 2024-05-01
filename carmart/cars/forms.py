from django import forms
from .models import CarsModel, Comment

class CarsForm(forms.ModelForm):
    class Meta:
        model = CarsModel
        exclude = ['author']
        # fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']