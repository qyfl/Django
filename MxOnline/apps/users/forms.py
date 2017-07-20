# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/16 18:47"

from django import forms
from captcha.fields import CaptchaField


# 登录
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
 
    
# 注册
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})

# 找回密码
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})
    
    
# 密码修改
class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True, min_length=5)
    password1 = forms.CharField(required=True, min_length=5)