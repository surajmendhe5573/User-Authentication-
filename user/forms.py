from django import forms
from .models import User
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user
