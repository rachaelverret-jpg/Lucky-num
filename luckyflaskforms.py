from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange, AnyOf

VALID_COLORS = ["red", "green", "orange", "blue"]


class LuckyNumberRequestForm(FlaskForm):
    """Form to request a lucky number."""

    class Meta:
        csrf = False

    name = StringField(
        "Name",
        validators=[InputRequired()]
    )

    email = StringField(
        "Email",
        validators=[InputRequired(), Email()]
    )

    year = IntegerField(
        "Year",
        validators=[NumberRange(1900, 2000)]
    )

    color = StringField(
        "Favorite Color",
        validators=[AnyOf(VALID_COLORS)]
    )
