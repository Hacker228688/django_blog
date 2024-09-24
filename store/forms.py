from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'slug', 'price', 'old_price', 'image',  'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
               'class': 'form-control'
            }),
            'old_price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'tags': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
