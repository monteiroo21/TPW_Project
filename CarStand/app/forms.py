from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.models import Brand, Car, CarModel, Profile


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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']


class GroupSearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800', 'placeholder': ('Search for a group')}))

class BrandSearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800', 'placeholder': ('Search for a brand')}))

class CarSortAndFilter(forms.Form):
    name = forms.CharField(
        max_length=100, required=False, widget=forms.TextInput(
        attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
                'placeholder': 'Search for a group',
                'style': 'background-image: url(/static/imgs/search.svg); background-repeat: no-repeat; background-position: 10px center; background-size: 18px;'
            }
            ),
            label=''
        )
    
    sort = forms.ChoiceField(
        choices=[
            ("1", "Sort by Brand"),
            ("2", "Sort by Price"),
            ("3", "Sort by Year")
        ],
        widget=forms.Select(attrs={'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'}),
        label=''
    )
    
    isElectric = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label=''
    )
    
    numberDoors = forms.ChoiceField(
        choices=[
            ("All", "All doors"),
            ("3", "3 doors"),
            ("5", "5 doors")
        ],
        widget=forms.Select(attrs={'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'}),
        label=''
    )

    newOrUsed = forms.ChoiceField(
        choices=[
            ("All", "New and Used"),
            ("true", "New Cars"),
            ("false", "Used cars")
        ],
        widget=forms.Select(attrs={'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'}),
        label=''
    )

    
    color = forms.ChoiceField(
        choices=[
            ("None", "All colors"),
            ("blue", "Blue"),
            ("red", "Red"),
            ("white", "White"),
            ("black", "Black"),
            ("grey", "Grey"),
            ("green", "Green")
        ],
        widget=forms.Select(attrs={'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'}),
        label=''
    )
  
    priceMax = forms.DecimalField(
        widget=forms.TextInput(attrs={'class':'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800','placeholder': 'Price Max'}),
        required=False,
        label=''
    )

    priceMin = forms.DecimalField(
        widget=forms.TextInput(attrs={'class':'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800','placeholder': 'Price Min'}),
        required=False,
        label=''
    )


class MotoSortAndFilter(forms.Form):
    name = forms.CharField(
        max_length=100, required=False, widget=forms.TextInput(
        attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
                'placeholder': 'Search for a group',
                'style': 'background-image: url(/static/imgs/search.svg); background-repeat: no-repeat; background-position: 10px center; background-size: 18px;'
            }
            ),
            label=''
        )
    
    sort = forms.ChoiceField(
        choices=[
            ("1", "Sort by Brand"),
            ("2", "Sort by Price"),
            ("3", "Sort by Year")
        ],
        widget=forms.Select(attrs={'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'}),
        label=''
    )


    newOrUsed = forms.ChoiceField(
        choices=[
            ("All", "New and Used"),
            ("true", "New motos"),
            ("false", "Used motos")
        ],
        widget=forms.Select(attrs={'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'}),
        label=''
    )

    
    color = forms.ChoiceField(
        choices=[
            ("None", "All colors"),
            ("blue", "Blue"),
            ("red", "Red"),
            ("white", "White"),
            ("black", "Black"),
            ("grey", "Grey"),
            ("green", "Green")
        ],
        widget=forms.Select(attrs={'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'}),
        label=''
    )
  
    priceMax = forms.DecimalField(
        widget=forms.TextInput(attrs={'class':'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800','placeholder': 'Price Max'}),
        required=False,
        label=''
    )

    priceMin = forms.DecimalField(
        widget=forms.TextInput(attrs={'class':'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800','placeholder': 'Price Min'}),
        required=False,
        label=''
    )

class CreateCar(forms.Form):
    model = forms.ModelChoiceField(
        queryset=CarModel.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'
        })
    )
    year = forms.IntegerField(
        min_value=1990, max_value=2024,
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Year'
        })
    )
    kilometers = forms.FloatField(
        required=False, min_value=0.0,
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Kilometers'
        })
    )
    price = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.TextInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Price'
        })
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'w-full py-2 px-3 border-2 border-gray-400 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800'
        })
    )
    color = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Color'
        })
    )
    doors = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Number of Doors'
        })
    )
    electric = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox h-5 w-5 text-blue-600 focus:ring-0'
        })
    )


class CreateCarModel(forms.Form):
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'
        })
    )
    name = forms.CharField(
        max_length=70,
        widget=forms.TextInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Model Name'
        })
    )
    base_price = forms.FloatField(
        min_value=0.0,
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Base Price'
        })
    )
    specifications = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full h-32 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Specifications'
        })
    )
    releaseYear = forms.IntegerField(
        min_value=1990, max_value=2024,
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Release Year'
        })
    )

    

class UpdateCar(forms.Form):
    model = forms.ModelChoiceField(
        queryset=CarModel.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline'
        })
    )
    year = forms.IntegerField(
        min_value=1990, max_value=2024,
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Year'
        })
    )
    kilometers = forms.FloatField(
        required=False, min_value=0.0,
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Kilometers'
        })
    )
    price = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.TextInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Price'
        })
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'w-full py-2 px-3 border-2 border-gray-400 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800'
        }),required=False
    )
    color = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Color'
        })
    )
    doors = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-80 pl-10 pr-4 py-2 border-2 border-sky-800 bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-800',
            'placeholder': 'Number of Doors'
        })
    )
    electric = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox h-5 w-5 text-blue-600 focus:ring-0'
        })
    )
