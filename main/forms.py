from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import CustomUser

class CreateApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__',
   
class EditApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__',

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
    