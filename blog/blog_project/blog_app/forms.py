from django import forms

class SignUpForm(forms.Form):
    fullname=forms.CharField()
    mailID=forms.EmailField()
    userName=forms.CharField()
    phNumber=forms.IntegerField()
    password=forms.CharField()