from logging import PlaceHolder
from django.db import models
from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'用户名'}))
    password = forms.CharField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'密码'}))
    captcha = CaptchaField(label='')

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'用户名'}))
    password1 = forms.CharField(label="", widget= forms.TextInput
                           (attrs={'placeholder':'密码'}))
    password2 = forms.CharField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'确认密码'}))
    email = forms.EmailField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'邮箱地址'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='')

class User(models.Model):
    '''用户表'''

    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
# Create your models here.
