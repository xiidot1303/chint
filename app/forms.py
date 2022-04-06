from django.forms import ModelForm, widgets
from app.models import *
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = {'title', 'description', 'photo', 'point'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', "style":"height: 200px;"}),
            'photo': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'point': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Название',
            'description': 'Описание',
            'photo': 'Фото',
            'point': 'Баллы',
        }

    field_order = ['title', 'point', 'description', 'photo']