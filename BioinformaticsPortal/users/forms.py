from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PortalUser

class PortalUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = PortalUser
        fields = ('username', 'email')


class PortalUserChangeForm(UserChangeForm):

    class Meta:
        model = PortalUser
        fields = UserChangeForm.Meta.fields
