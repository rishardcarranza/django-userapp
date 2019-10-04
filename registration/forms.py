from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'name', 'lastname', 'avatar', 'aboutme', 'link']
        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control mt-3', 'placeholder' : 'Nombre de usuario'}),
            'name' : forms.TextInput(attrs = {'class' : 'form-control mt-3', 'placeholder' : 'Nombres'}),
            'lastname' : forms.TextInput(attrs = {'class' : 'form-control mt-3', 'placeholder' : 'Apellidos'}),
            'avatar' : forms.ClearableFileInput(attrs = {'class' : 'form-control-file mt-3'}),
            'aboutme' : forms.Textarea(attrs = {'class' : 'form-control mt-3', 'rows' : 3, 'placeholder' : 'Sorbre mi'}),
            'link' : forms.URLInput(attrs = {'class' : 'form-control mt-3', 'placeholder' : 'Web personal o sitio web'}),
        }