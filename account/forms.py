from django.contrib.auth.forms import AuthenticationForm
from django import forms
class login(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(login, self).__init__(*args, **kwargs)
        username = forms.EmailField(widget=forms.TextInput(
            attrs={
                'label': 'Email',
                'class': 'form-control',
                'placeholder': '',
                'id': 'username'
            }
        ))
        password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'label': 'senha',
                'class': 'form-control',
                'placeholder': '',
                'id': 'password',
            }
        ))
