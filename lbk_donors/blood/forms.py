from django import forms
from .models import RegistrationForm
from django.contrib.auth.forms import PasswordResetForm


class MyRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegistrationForm
        fields = ["name", "age", "bloodgroup", "native", "contact", "email","donated_date"]
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)