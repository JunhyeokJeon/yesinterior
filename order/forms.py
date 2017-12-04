from order.models import Order
from django import forms

class DoOrderForm(forms.ModelForm):
    phone = forms.CharField(
        label = "휴대폰 번호",
        help_text = "필수입력 사항은 아닙니다. 빠른 소통을 원하신다면 입력해 주세요. ('-'와 숫자만 입력해주세요.)",
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'ex) 010-xxxx-xxxx',
                'required': 'true'
            }),
        )
    date = forms.CharField(
        label = "예상 공사시작 날짜",
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'ex) 2017-12-01',
                'required': 'true'
            }),
        )
    email = forms.EmailField(
        label = "E-mail",
        help_text = "E-mail을 입력해주세요.",
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'ex) nav123@nav.co.kr',
                'required': 'true'
            }),
        )

    class Meta:
        model = Order
        fields = ('title', 'location', 'date', 'image', 'description', 'name', 'phone', 'email')
