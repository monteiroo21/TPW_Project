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

class CarSortAndFilter(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o seu nome'}),
        required=False
    )
    
    sort = forms.ChoiceField(
        choices=[
            ("1", "Sort by Brand"),
            ("2", "Sort by Price"),
            ("3", "Sort by Year")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    isElectric = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    numberDoors = forms.ChoiceField(
        choices=[
            ("All", "All doors"),
            ("3", "3 doors"),
            ("5", "5 doors")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    newOrUsed = forms.ChoiceField(
        choices=[
            ("All", "All cars"),
            ("true", "New Cars"),
            ("false", "Used cars")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    
    color = forms.ChoiceField(
        choices=[
            ("None", "None"),
            ("blue", "blue"),
            ("red", "red"),
            ("white", "white"),
            ("black", "black"),
            ("grey", "grey"),
            ("green", "green")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
  
    priceMax = forms.DecimalField(
        widget=forms.TextInput(attrs={'placeholder': 'Price Max'}),
        required=False
    )

    priceMin = forms.DecimalField(
        widget=forms.TextInput(attrs={'placeholder': 'Price Max'}),
        required=False,

    )