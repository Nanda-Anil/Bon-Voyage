from django.contrib.auth.models import User

from .models import *
from django import forms

class agencyregform(forms.Form):
    agency=forms.CharField(max_length=20)
    email=forms.EmailField()
    address=forms.CharField(max_length=300)
    phone=forms.IntegerField()
    password=forms.CharField(max_length=10)
    cpassword = forms.CharField(max_length=10)

class agencylogform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=10)

# class uploadform(forms.Form):
#     agency=forms.CharField(max_length=30)
#     email = forms.EmailField()
#     destinations = forms.CharField(max_length=300)
#     days = forms.CharField(max_length=30)
#     nights = forms.CharField(max_length=30)
#     stay = forms.CharField(max_length=30)
#     pet = forms.CharField(max_length=30)
#     food = forms.CharField(max_length=30)
#     rate =forms.CharField(max_length=30)

class uploadform(forms.Form):
    agency=forms.CharField(max_length=20)
    email = forms.EmailField()
    destina= forms.CharField(max_length=20)
    food= forms.CharField(max_length=20)
    pet = forms.CharField(max_length=20)
    duration = forms.CharField(max_length=20)
    stay = forms.CharField(max_length=20)
    rate = forms.CharField(max_length=20)



# class userreg(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=["username","email","password","first_name","last_name"]
#
# class userlog(forms.Form):
#     email=forms.EmailField()
#     password=forms.CharField(max_length=10)

class userregform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)

class userlogform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class bookform(forms.Form):
    agency=forms.CharField(max_length=20)
    destina=forms.CharField(max_length=20)
    rate = forms.CharField(max_length=20)
    name=forms.CharField(max_length=20)
    email=forms.EmailField()

class confirmationemailform(forms.Form):
    email=forms.EmailField()
    message=forms.CharField(max_length=200)