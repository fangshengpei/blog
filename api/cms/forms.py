#coding:utf-8

from django import forms
from utils.captcha.pfscaptcha import Captcha

class LoginForm(forms.Form):
	username=forms.CharField(max_length=20,min_length=4)
	password=forms.CharField(max_length=20,min_length=6)
	captcha=forms.CharField(max_length=4,min_length=4)
	def clean_captcha(self):
		captcha=self.cleaned_data.get('captcha',None)
		if Captcha.check_captcha(captcha):
			return captcha
		else:
			raise forms.ValidationError(u'验证码错误')