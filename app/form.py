from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Regexp, Length

class LoginForm(FlaskForm):
    email = StringField("", 
    		[ DataRequired(), Email(message=("Correo Incorrecto"), granular_message=False)],
    		render_kw={"class":"form-control", "aria-describedby":"emailHelp", "placeholder": "Email"})
    password = PasswordField("",
    		[DataRequired(), Length(8, 255, message='Debe contener al menos 8 caracteres')],
    		render_kw={"class":"form-control", "aria-describedby":"passwordHelp", "placeholder": "Contraseña"})


class SiginForm(FlaskForm):
    name = StringField("",
    		[DataRequired(), Length(min=4, max=20, message="Debe contener de 4 a 20 caracteres"), Regexp(regex='[a-zA-z]', message="El nombre solo puede empezar con una letra de la A a la Z")], 
    		render_kw={"class":"form-control", "placeholder":"Nombre y Apellidos"})
    email = StringField("",
    		[DataRequired(), Email(message=("Correo Incorrecto"), granular_message=False)],
    		render_kw={"class":"form-control", "aria-describedby":"emailHelp", "placeholder": "Email"})
    password = PasswordField("",
    		[DataRequired(), Length(8, 255, message='Debe contener al menos 8 caracteres')],
    		render_kw={"class":"form-control", "aria-describedby":"passwordHelp", "placeholder": "Contraseña"})
    confirm = PasswordField("",
    		[DataRequired(), EqualTo('password', message=("Contraseñas deben coincidir"))],
    		render_kw={"class":"form-control", "aria-describedby":"passwordHelp", "placeholder": "Repetir Contraseña"})
    #remember = BooleanField("Remember Me")
    #submit = SubmitField()

class SignForm_school(FlaskForm):
    name = StringField("",
    		[DataRequired()],
    		render_kw={"class":"form-control", "placeholder":"Nombre de la Escuela"})
    location = StringField("",
    		[DataRequired()],
    		render_kw={"class":"form-control", "placeholder": "Dirección"})
    students_num = IntegerField("",
    		[DataRequired()],
    		render_kw={"class":"form-control", "placeholder": "Número de Estudiantes"})
    type_s = StringField("",
    		[DataRequired()],
    		render_kw={"class":"form-control", "placeholder": "Tipo"})
    #remember = BooleanField("Remember Me")
    #submit = SubmitField()

class SignForm_player(FlaskForm):
    name = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder":"Nombre y Apellido"})
    age = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Edad"})
    level = IntegerField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Grado de Educación"})
    school = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Escuela"})

class SignForm_game(FlaskForm):
    name = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder":"Nombre del Juego"})
    category = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Categoría"})
    level = IntegerField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Nivel"})
    rating = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Rating"})

class SignForm_tutor(FlaskForm):
    name = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder":"Nombre y Apellido"})
    category = StringField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Edad"})
    level = IntegerField("",
            [DataRequired()],
            render_kw={"class":"form-control", "placeholder": "Teléfono"})

