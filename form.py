from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField("", [DataRequired(), Email(message=("Correo Incorrecto"), granular_message=False)], render_kw={"class":"form-control", "aria-describedby":"emailHelp", "placeholder": "Email"})
    password = PasswordField("", [DataRequired()], render_kw={"class":"form-control", "aria-describedby":"passwordHelp", "placeholder": "Contraseña"})


class SiginForm(FlaskForm):
    name = StringField("", [DataRequired()], render_kw={"class":"form-control", "placeholder":"Nombre y Apellido"})
    email = StringField("", [DataRequired(), Email(message=("Correo Incorrecto"), granular_message=False)], render_kw={"class":"form-control", "aria-describedby":"emailHelp", "placeholder": "Email"})
    password = PasswordField("", [DataRequired()], render_kw={"class":"form-control", "aria-describedby":"passwordHelp", "placeholder": "Contraseña"})
    confirm = PasswordField("", [DataRequired(), EqualTo('password', message=('Contraseñas deben coincidir.'))], render_kw={"class":"form-control", "aria-describedby":"passwordHelp", "placeholder": "Repetir Contraseña"})
    #remember = BooleanField("Remember Me")
    #submit = SubmitField()

class SignForm_school(FlaskForm):
    name = StringField("", [DataRequired()], render_kw={"class":"form-control", "placeholder":"Nombre de la Escuela"})
    location = StringField("", [DataRequired()], render_kw={"class":"form-control", "placeholder": "Dirección"})
    students_num = IntegerField("", [DataRequired()], render_kw={"class":"form-control", "placeholder": "Número de Estudiantes"})
    type_s = StringField("", [DataRequired()], render_kw={"class":"form-control", "placeholder": "Tipo"})
    #remember = BooleanField("Remember Me")
    #submit = SubmitField()