from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'age', 'is_staff', 'national_code',
                  'address', 'postal_code', 'province', 'city', 'gender',]
    list_editable = ['email', 'age', 'is_staff', 'national_code',
                  'address', 'postal_code', 'province', 'city', 'gender',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'national_code',
                  'address', 'postal_code', 'province', 'city', 'gender')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'national_code',
                  'address', 'postal_code', 'province', 'city', 'gender')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
