from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import AppointmentDetails, Contact



class AppointmentForm(forms.ModelForm):

    class Meta:
        model = AppointmentDetails
        labels = {'name': 'Name', 'email': 'Email', 'mob_no': 'Mobile No.', 'consultant': 'Consultant',}

        fields='__all__'
        # fields = ['name', 'email', 'mob_no','consultant','date','slot']
        # labels = {'name': 'Name', 'email': 'Email', 'mob_no': 'Mobile No.', 'consultant': 'Consultant',
        #           'date': 'Date', 'slot':'Slot'}

        # widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
        #            'mob_no': forms.TextInput(attrs={'class': 'form-control'}),
        #            'consultant': forms.TextInput(attrs={'class': 'form-control'}),
        #            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #            'date': forms.DateInput(attrs={'class': 'form-control'}),
        #            'slot': forms.TimeInput(attrs={'class': 'form-control'}),
        #            }

# class SignupForm(UserCreationForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Confirm Password(again)',
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#         labels = {'username': 'Username', 'email': 'Email'}
#         widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
#                    'email': forms.EmailInput(attrs={'class': 'form-control'})
#                    }
#

#class SignupForm(forms.ModelForm):
class SignupForm(UserCreationForm):
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(label='Confirm Password(again)',
    #                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        labels = {'username': 'Username', 'email': 'Email','password1':'Password','password2':'Confirm Password'}
# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
#     password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        label = {'name':'Name', 'email':'Email', 'phone':'Phone', 'message': 'Message'}