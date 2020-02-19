from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ContatoForm(FlaskForm):
    nome = StringField('Nome:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])