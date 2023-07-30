from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

class RegForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Ім\'я користувача'
            }),
            'password': TextInput(attrs={
                'placeholder': 'Пароль',
                'type': 'password'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Email',
                'type': 'email'
            }),
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Ім\'я користувача'
            }),
            'password': TextInput(attrs={
                'placeholder': 'Пароль',
                'type': 'password'
            }),
        }
        