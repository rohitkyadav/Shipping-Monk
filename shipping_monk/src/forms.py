from django import forms
from .models import SignUp
from django import forms as forms
from django.forms import ModelForm
from .models import orderDetail,shop

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email  = forms.EmailField() 
	message = forms.CharField()
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domail, extension = provider.split(".")
		if not extension == "com":
			raise forms.ValidationError("Please use a valid .com email address")
		return email

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domail, extension = provider.split(".")
		if not extension == "com":
			raise forms.ValidationError("Please use a valid .com email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

class orderDetailForm(ModelForm):
	class Meta:
		model = orderDetail
		fields = ['Name','Address','orderId']

class shopForm(ModelForm):
	class Meta:
		model = shop
		fields = ['hname','hubId','address','Auth_to','email','phone_number']