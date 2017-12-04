from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.RegexField(
        label = "아이디",
        max_length = 30,
        regex = r'^[\w.@+-]+$',
        help_text = "소문자, 숫자, '@\.\+\-\_'만 사용할 수 있으며, 30자 안으로 입력해 주세요.",
        error_messages = { 'invalid': 'id가 중복되었거나 잘못된 문자를 입력하셨습니다. 다시 입력해주세요.' },
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'id를 입력해주세요.',
                'required': 'true'
            }),
        )

    class Meta: # CreateUserForm에 대한 기술서
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # ↑모든 필드를 다 보여주고 싶다면, 각각의 필등명이 아닌 "__all__"이라고 적어주면 됨.

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length = 30,
        label = '아이디',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'id를 입력해주세요.',
                'required': 'true'
            }
        )
    )

    password = forms.CharField(
        label = '비밀번호',
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': '비밀번호를 입력해주세요.',
                'required': 'true'
            }
        )
    )
