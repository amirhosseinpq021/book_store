from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [
        (True, 'مرد'),
        (False, 'زن'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="جنسیت"
    )

    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'national_code',
                  'address', 'postal_code', 'province', 'city', 'gender')

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

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if gender is None:
            raise forms.ValidationError("لطفاً جنسیت خود را مشخص کنید.")
        return gender


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'national_code',
                  'address', 'postal_code', 'province', 'city', )
