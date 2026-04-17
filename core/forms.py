from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ismingiz',
                'id': 'nameInput',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'email@example.com',
                'id': 'emailInput',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': "Xabaringizni yozing...",
                'id': 'msgInput',
            }),
        }
