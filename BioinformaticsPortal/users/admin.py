from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import AdminPortalUserCreationForm, AdminPortalUserChangeForm
from .models import PortalUser
from django.utils.translation import gettext_lazy as _


class PortalUserAdmin(UserAdmin):
    model = PortalUser
    add_form = AdminPortalUserCreationForm
    form = AdminPortalUserChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (_('Login Info'), {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('last_name', 'first_name', 'email', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')



admin.site.register(PortalUser, PortalUserAdmin)
