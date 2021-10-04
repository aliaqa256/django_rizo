from django import forms
from cms.models import ticket
from cms.forms.messages import messages

class NewTicketForm(forms.Form):
    choice = forms.ChoiceField(choices=(('پشتیبانی',('پشتیبانی')),('پیشنهاد',('پیشنهاد')),('همکاری',('همکاری')),('باگ',('باگ'))),label='درخواست',error_messages=messages,widget=forms.Select(attrs={'class':'form-control center'}))
    title = forms.CharField(error_messages=messages,label="سربرگ",widget=forms.TextInput(attrs={'class':'form-control center','placeholder':'سربرگ'}))
    mozoee = forms.CharField(error_messages=messages,label="موضوع",widget=forms.TextInput(attrs={'class':'form-control center','placeholder':'موضوع'}))
    des = forms.CharField(error_messages=messages,label="متن",widget=forms.Textarea(attrs={'class':'form-control center','placeholder':'توضیحات'}))
    
class TicketForm(forms.Form):
    des = forms.CharField(error_messages=messages,label="متن",widget=forms.Textarea(attrs={'class':'form-control center','placeholder':'توضیحات'}))
