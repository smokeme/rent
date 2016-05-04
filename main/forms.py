from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import CustomUser, Apartment
from django.db import models

class EmailForm(forms.Form):
	firstname = forms.CharField(max_length=255)
	lastname = forms.CharField(max_length=255)
	email = forms.EmailField()
	subject = forms.CharField(max_length=255)
	# botcheck = forms.CharField(max_length=5)
	message = forms.CharField()

class Searchbox(forms.ModelForm):
    parking = forms.IntegerField(required=False)
    internet = forms.BooleanField(required=False)
    pets = forms.BooleanField(required=False)
    maidroom = forms.BooleanField(required=False)
    lift = forms.BooleanField(required=False)
    balcony = forms.BooleanField(required=False)
    bills = forms.BooleanField(required=False)
    class Meta:
        model = Apartment
        fields = ['area',]

class CreateApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
   
class EditApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)

	class Meta:
		model = CustomUser
		fields = ("email",)

	class CustomUserChangeForm(UserChangeForm):
		def __init__(self, *args, **kwargs):
			super(CustomUserChangeForm, self).__init__(*args, **kwargs)
			del self.fields['username']

		class Meta:
			model = CustomUser
			fields = '__all__'

class CustomUserLoginForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']
    