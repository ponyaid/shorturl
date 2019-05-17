from wtforms import Form, StringField
from wtforms.validators import DataRequired, URL


class LinkForm(Form):
    full_link = StringField(
        'Full link',
        [
            DataRequired(),
            URL(require_tld=False, message='URL не валидный.')
        ]
    )
