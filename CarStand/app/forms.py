from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class GroupSearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800', 'placeholder': ('Search for a group')}))
