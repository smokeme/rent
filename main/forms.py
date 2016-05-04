from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import CustomUser, Apartment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions

class Searchbox(forms.ModelForm):
    parking = forms.IntegerField(required=False)
    internet = forms.BooleanField(required=False)
    pets = forms.BooleanField(required=False)
    maidroom = forms.BooleanField(required=False)
    lift = forms.BooleanField(required=False)
    balcony = forms.BooleanField(required=False)
    bills = forms.BooleanField(required=False)
    livingroom = forms.IntegerField(required=False)
    bathroom = forms.IntegerField(required=False)
    minprice = forms.IntegerField(required=False)
    maxprice = forms.IntegerField(required=False)
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


# class EditProfileForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'name', 'mobile']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/edit_profile/'
        self.helper.help_text_inline = True
        self.helper.error_text_inline = True
        # self.helper.html5_required = True
        self.helper.layout = Layout(
                Div('first_name', 'email', 'last_name',
                    FormActions(
                        Submit('submit', 'Register Now', css_class="btn-primary")
                        ),
                    ), #css_class='col-md-6'
                Div('message', css_class='col-md-12')
                )
    