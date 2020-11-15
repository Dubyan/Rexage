from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Tour
from django.forms import ModelForm, Textarea, TextInput



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    field_order = ['username', 'password1', 'password2']


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ["Туроператор", "Где_остановиться", "Где_поесть", "Комментарий"]
        widgets = {"Туроператор":TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Небо56 / А-Трэвл / Большие гонки'
        }),
            "Где_остановиться": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Виктория / Дубрава Плюс / Золотой Дракон / Золотой Слон / Зорянка / Старый Маяк / Hilton Garden inn Orenburg'
            }),
        "Где_поесть": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Макдоналдс / Имбирь / Пахлава / Шашлычная Тандыр / Coffee Like / Роял Палас / Роза Ветров'
        }),
        "Комментарий": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Комментарий'
        }),


                   }