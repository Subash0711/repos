from django import forms

class ResgistrationForm(forms.Form):
    Name = forms.CharField(max_length=100, required=True)
    Email = forms.EmailField(required=True)
    Mobile = forms.CharField(max_length=20, required=True)
    Nationality = forms.CharField(max_length=100, required=True)
    Country = forms.CharField(max_length=100, required=True)
    Role = forms.ChoiceField(choices=
        [('Admin', 'Admin'), 
        ('Student', 'Student'), 
        ('Staff', 'Staff'), 
        ('Editor', 'Editor')], required=True)
    Password = forms.CharField(widget=forms.PasswordInput, required=True)