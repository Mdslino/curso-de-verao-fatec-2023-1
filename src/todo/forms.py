from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired()])
    description = StringField("Descrição", validators=[DataRequired()])
    is_done = BooleanField("Concluído")
    submit = SubmitField("Criar")
