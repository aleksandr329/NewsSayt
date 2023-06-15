from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, mail_managers, mail_admins


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        subject = 'Добро пожаловать в наш интернет-магазин!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/main">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_managers(
            subject='Эй Менеджер у нас Новый пользователь!',
            message=f'Пользователь {user.username}, вот его почтовый адрес {user.email}зарегистрировался на сайте.'
        )

        mail_admins(
            subject='Эй Админ у нас Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return



    def mailing_list(self, request, instance=None, user=None):
        emails = User.objects.filter(
                     subscriptions__category=instance.category
                 ).values_list('email', flat=True)
        subject = 'Последние новости на эту неделю'
        text = f'Я не знаю как сделать правильный GET запрос чтобы получить последние новости и возможно мейл адреса я тоже неправильно написал'

        for email in emails:
            msg = EmailMultiAlternatives(subject, text, None, [email])
            msg.send()

        return user

