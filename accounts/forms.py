from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'national_code',
                  'address', 'postal_code', 'province', 'city',)

        help_texts = {
            'username': 'لطفا شامل حروف بزرگ و کوچک و عددی باشد',  # حذف متن راهنما
            'email': 'لطفاایمیل معتبر وارد کنید ',
            'age': 'سن واقعی خودتان را وارد کنید',
            'password confirmation': 'تکرار رمز عبور را صحیح وارد کنید',
            'password': 'شامل حروف بزرگ و کوچک و عدد باشد',
        }

    def __init__(self, *args, **kwargs):  # delete password help text
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'national_code',
                  'address', 'postal_code', 'province', 'city', )
