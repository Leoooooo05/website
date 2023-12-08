from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Item
INPUT_CLASSES="w-full py-4 px-6 rounded-xl"

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')
        widgets={
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
                }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),   
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
                }),    
            'price':forms.NumberInput(attrs={
                'class':INPUT_CLASSES
                }),    
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
                }), 
        }
class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=('username','password')

    username= forms.CharField (widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password= forms.CharField (widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username','email','password1','password2')

    username= forms.CharField (widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    email= forms.CharField (widget=forms.EmailInput(attrs={
        'placeholder':'Your Email',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password1= forms.CharField (widget=forms.PasswordInput(attrs={
        'placeholder':'Your Password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password2= forms.CharField (widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))

class EditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')
        widgets={
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
                }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),   
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
                }),    
            'price':forms.NumberInput(attrs={
                'class':INPUT_CLASSES
                }),    
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
                }), 
        }