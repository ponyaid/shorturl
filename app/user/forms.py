from wtforms import Form, StringField, PasswordField, BooleanField
from wtforms.validators import Email, DataRequired, EqualTo, Length, ValidationError

from app.models import User


class LoginForm(Form):
    email = StringField(
        'Email адрес',
        [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Пароль',
        [
            DataRequired()
        ]
    )
    remember_me = BooleanField('Запомнить меня')


class SignupForm(Form):
    username = StringField(
        'Username',
        [
            DataRequired(),
            Length(min=5, message='Минимальное к-во символов 5, максимальное - 32.')
        ]
    )
    email = StringField(
        'Email адрес',
        [
            DataRequired(),
            Length(max=64, message='Максимальное к-во символов 64.'),
            Email()
        ]
    )
    password = PasswordField(
        'Пароль',
        [
            DataRequired(),
            Length(min=8, max=32, message='Минимальное к-во символов 8, максимальное - 32.')
        ]
    )
    password2 = StringField(
        'Повторите пароль',
        [
            DataRequired(),
            EqualTo('password', message='Пароли не совпадают.')
        ]
    )

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другой username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другой email.')
