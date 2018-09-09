from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        models = User
        fields = ('username','first_name','last_name','password1',)
    
    def save(self, commit=True):
        user=super(RegistrationForm, self).save(commit=False)
        user.first_name = cleaned_data['first_name']
        user.last_name = cleaned_data['last_name']
        user.email=cleaned_data['email']

        if commit:
            user.save
        return user
        