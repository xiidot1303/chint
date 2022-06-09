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


class UploadFileFrom(forms.Form):
    file = forms.FileField(allow_empty_file=False, required=True, label='Файл', widget = forms.FileInput(attrs={'class': 'custom-file-input'}))

class UserChangePointForm(forms.Form):
    point = forms.CharField(required=True, max_length=100, label='Баллы', widget=forms.NumberInput(attrs={'class': 'form-control'}))


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = {'file_ru', 'file_uz', 'contact_ru', 'contact_uz', 'company_name', 'company_about', 'phone1', 'phone2', 
            'site', 'instagram', 'facebook', 'telegram', 'youtube', 'telegram_username'}
        
        widgets = {
            'file_ru': forms.FileInput(attrs={'class': 'custom-file-input'}), 
            'file_uz': forms.FileInput(attrs={'class': 'custom-file-input'}), 
            'contact_ru': forms.Textarea(attrs={'class': 'form-control', "style":"height: 200px;"}), 
            'contact_uz': forms.Textarea(attrs={'class': 'form-control', "style":"height: 200px;"}), 
            'company_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'company_about': forms.TextInput(attrs={'class': 'form-control'}), 
            'phone1': forms.TextInput(attrs={'class': 'form-control'}), 
            'phone2': forms.TextInput(attrs={'class': 'form-control'}), 
            'telegram_username': forms.TextInput(attrs={'class': 'form-control'}), 
            'site': forms.TextInput(attrs={'class': 'form-control'}), 
            'instagram': forms.TextInput(attrs={'class': 'form-control'}), 
            'facebook': forms.TextInput(attrs={'class': 'form-control'}), 
            'telegram': forms.TextInput(attrs={'class': 'form-control'}), 
            'youtube': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'file_ru': 'Файл для акции (RU)', 
            'file_uz': 'Файл для акции (UZ)', 
            'contact_ru': 'Наши контакты (RU)', 
            'contact_uz': 'Наши контакты (UZ)', 
            'company_name': 'Название компании', 
            'company_about': 'О компании', 
            'phone1': 'Телефон 1', 
            'phone2': 'Телефон 2', 
            'telegram_username': 'Модератор', 
            'site': 'Сайт', 
            'instagram': 'Instagram', 
            'facebook': 'Faceboook', 
            'telegram': 'Telegram', 
            'youtube': 'Youtube'
        }
    field_order = ['file_ru', 'file_uz', 'contact_ru', 'contact_uz', 'company_name', 'company_about', 'phone1', 'phone2', 'telegram_username',
        'site', 'instagram', 'facebook', 'telegram', 'youtube']


class RuleForm(ModelForm):
    class Meta:
        model = Rule
        fields = {'file_uz', 'file_ru', 'text_uz', 'text_ru'}

        widgets = {
            'file_uz': forms.FileInput(attrs={'class': 'custom-file-input'}), 
            'file_ru': forms.FileInput(attrs={'class': 'custom-file-input'}), 
            'text_uz': forms.Textarea(attrs={'class': 'form-control'}), 
            'text_ru': forms.Textarea(attrs={'class': 'form-control'})
        }

        labels = {
            'file_uz': 'Файл (UZ)', 
            'file_ru': 'Файл (RU)', 
            'text_uz': 'Текст (UZ)', 
            'text_ru': 'Текст (RU)'
        }
    field_order = ['file_uz', 'file_ru', 'text_uz', 'text_ru']



class PrizeForm(ModelForm):
    class Meta:
        model = Prize
        fields = {'title', 'title_uz', 'description', 'description_uz', 'photo', 'point'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', "style":"height: 200px;"}),
            'description_uz': forms.Textarea(attrs={'class': 'form-control', "style":"height: 200px;"}),
            'photo': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'point': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Название (RU)',
            'title_uz': 'Название (UZ)',
            'description': 'Описание (RU)',
            'description_uz': 'Описание (UZ)',
            'photo': 'Фото',
            'point': 'Баллы',
        }

    field_order = ['title', 'title_uz', 'description', 'description_uz', 'point', 'photo']