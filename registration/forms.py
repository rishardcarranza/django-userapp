from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text = 'El correo debe ser válido y con 254 caracteres como máximo')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # To verify if the email exists 
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('El usuario con ese correo ya existe')

        return email