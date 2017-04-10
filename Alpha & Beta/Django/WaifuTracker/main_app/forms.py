from django import forms
from .models import Waifu


class WaifuForm(forms.ModelForm):
	class Meta:
		model = Waifu
		fields = ['name', 'series', 'rating', 'height', 'image']


class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', max_length=30)
	password = forms.CharField(widget=forms.PasswordInput())
