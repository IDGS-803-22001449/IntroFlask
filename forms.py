from wtforms import Form 
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Regexp
from wtforms import StringField, EmailField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField

class UserForm(Form):
    matricula=SelectField("Matricula")
    edad=IntegerField("Edad")
    nombre=StringField("Nombre")
    apellidos=StringField("Apellidos")
    correo=EmailField("Correo")