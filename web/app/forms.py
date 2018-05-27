from wtforms import Form
from wtforms import StringField, TextAreaField, PasswordField, IntegerField, SelectField, BooleanField
from wtforms import validators

class LoginForm(Form):
    username = StringField('Username', [
            validators.Length(min=4, max=25)
        ],
        render_kw = {
            'maxlength': 25
        }
    )
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=5, max=25)
    ])
