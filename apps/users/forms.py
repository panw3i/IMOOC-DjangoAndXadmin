# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-01-18 14:20'
from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username=forms.CharField(required=True);
    password=forms.CharField(required=True,min_length=6);


class RegisterForm(forms.Form):
    email=forms.EmailField(required=True);
    password = forms.CharField(required=True, min_length=6);
    captcha=CaptchaField(error_messages={"invalid":u"验证码错误"});


class ForgetForm(forms.Form):
    email=forms.EmailField(required=True);
    captcha=CaptchaField(error_messages={"invalid":u"验证码错误"});


class ModifyPwdForm(forms.Form):
    password=forms.CharField(required=True,min_length=6);
    password2 = forms.CharField(required=True, min_length=6);
    captcha=CaptchaField(error_messages={"invalid":u"验证码错误"});


class UpdatePwdForm(forms.Form):
    password1=forms.CharField(required=True,min_length=6);
    password2=forms.CharField(required=True,min_length=6);


class UploadImageForm(forms.ModelForm):
    class Meta:
        model=UserProfile;
        fields=['image'];


class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfile;
        fields=['nick_name','gender','birday','address','mobile'];

