from .forms import UserCreationFormWithEmail, ProfileForm
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.http.response import HttpResponseRedirect

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        # Customize the form
        form.fields['username'].widget = forms.TextInput(attrs = {'class' : 'form-control mb-2', 'placeholder' : 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs = {'class' : 'form-control mb-2', 'placeholder' : 'Correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs = {'class' : 'form-control mb-2', 'placeholder' : 'Digite contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs = {'class' : 'form-control mb-2', 'placeholder' : 'Repita contraseña'})
    
        return form

@method_decorator(login_required, name = 'dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    # success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    user_requested = None

    def get_object(self):
        if self.kwargs:
            self.user_requested = User.objects.get(username = self.kwargs['username'])
            self.request.user = self.user_requested
        else:
            self.user_requested = self.request.user

        # Get the object to edit
        profile, created = Profile.objects.get_or_create(user = self.user_requested)
        profile.username = self.request.user.username

        return profile
    
    def get_success_url(self):
        return reverse_lazy('profile') + self.user_requested.username

@method_decorator(login_required, name = 'dispatch')
class ProfileList(ListView):
    model = Profile

@method_decorator(login_required, name = 'dispatch')
class ProfileDelete(DeleteView):
    model = Profile

    def delete(self, request, *args, **kwargs):
        user_to_delete = Profile.objects.get(pk = self.kwargs['pk']).user
        user_obj = User.objects.get(username = user_to_delete)
        user_obj.delete()
        print(user_obj)
        # user_to_delete = 
        return HttpResponseRedirect(reverse_lazy('list'))

        



