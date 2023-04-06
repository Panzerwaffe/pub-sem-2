from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from .models import Something


class SomethingForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired(), Length(min=5, max=100)])
    rating = IntegerField('Рейтинг', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Создать')

    def validate_name(self, name):
        print('Here we go')
        name = Something.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError('Такое уже есть')

class UpdateSomething(FlaskForm):
    rating = IntegerField('рейтинг', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Запулить')