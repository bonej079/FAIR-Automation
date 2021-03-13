from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PortalUser
from allauth.account.forms import SignupForm


class PortalUserCreationForm(SignupForm):
    first_name = forms.CharField(max_length=250, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name = forms.CharField(max_length=250, label='Surname', widget=forms.TextInput(attrs={'placeholder': 'Surname'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class AdminPortalUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = PortalUser
        fields = ('email', 'first_name', 'last_name')


class AdminPortalUserChangeForm(UserChangeForm):

    class Meta:
        model = PortalUser
        fields = UserChangeForm.Meta.fields
