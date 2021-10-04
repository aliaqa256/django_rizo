from django import forms
from cms.models import User
from cms.forms.messages import messages
class UserRegistrationForm(forms.Form):
    email = forms.EmailField(error_messages=messages,min_length=6,max_length=250,label="ایمیل",widget=forms.EmailInput(attrs={'class':'form-control center','autocomplete':'off','placeholder':'ایمیل'}),required=True)
    password = forms.CharField(error_messages=messages,min_length=8,max_length=100,label="پسورد",widget=forms.PasswordInput(attrs={'class':'form-control center','autocomplete':'off','placeholder':'پسورد'}),required=True)
    repassword = forms.CharField(error_messages=messages,min_length=8,max_length=100,label="تکرار پسورد",widget=forms.PasswordInput(attrs={'class':'form-control center','autocomplete':'off','placeholder':'تکرار پسورد'}),required=True)
    
class UserLoginForm(forms.Form):
    email = forms.EmailField(error_messages=messages,min_length=6,max_length=250,label="ایمیل ",widget=forms.EmailInput(attrs={'class':'form-control center','placeholder':'ایمیل'}),required=True)
    password = forms.CharField(error_messages=messages,min_length=8,max_length=100,label="پسورد ",widget=forms.PasswordInput(attrs={'class':'form-control center','placeholder':'کلمه عبور'}),required=True)
 
class RestPasswordForm(forms.Form):
    email = forms.EmailField(error_messages=messages,min_length=6,max_length=250,label="ایمیل ",widget=forms.EmailInput(attrs={'class':'form-control center','placeholder':'ایمیل'}),required=True)

class ChangeRestPasswordForm(forms.Form):
    password = forms.CharField(error_messages=messages,max_length=100,min_length=8,label='پسورد',widget=forms.PasswordInput(attrs={'class':'form-control center','placeholder':'پسورد'}),required=True)
    repassword = forms.CharField(error_messages=messages,max_length=100,min_length=8,label='تکرار پسورد',widget=forms.PasswordInput(attrs={'class':'form-control center','placeholder':'تکرار پسورد'}),required=True)
    
class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(error_messages=messages,min_length=8,max_length=100,label='پسورد',widget=forms.PasswordInput(attrs={'class':'form-control  center','placeholder':'پسورد'}),required=True)
    password = forms.CharField(error_messages=messages,min_length=8,max_length=100,label='پسورد جدید',widget=forms.PasswordInput(attrs={'class':'form-control center','placeholder':'پسورد جدید'}),required=True)
    repassword = forms.CharField(error_messages=messages,min_length=8,max_length=100,label='تکرار پسورد جدید',widget=forms.PasswordInput(attrs={'class':'form-control center','placeholder':'تکرار پسورد جدید'}),required=True)


class FormProfile(forms.ModelForm):
    profile_img = forms.ImageField(error_messages=messages,label="عکس پروفایل",widget=forms.FileInput(attrs={'class':'form-control-file center'}))
    firstname = forms.CharField(error_messages=messages,label="نام",widget=forms.TextInput(attrs={'class':'form-control center','placeholder':'نام'}))
    lastname = forms.CharField(error_messages=messages,label="نام خانوادگی",widget=forms.TextInput(attrs={'class':'form-control center','placeholder':'نام خانوادگی'}))    
    class Meta:
        model = User
        fields = ['profile_img','firstname','lastname',]