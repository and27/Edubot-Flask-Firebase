from flask import Flask, render_template, request, redirect, session, url_for
from functools import wraps
from rank_dic import rank_dic 
from game_dic import game_dic
#from views.api_player import edubot
from views.api_school import edubot
import pyrebase
from form import SiginForm, LoginForm
import os

app = Flask(__name__)

#import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

firebaseConfig = {
    "apiKey": "AIzaSyCbdZiJXL23Cy3hozapwNzl_QDJ7SQXZYQ",
    "authDomain": "edubot-f2362.firebaseapp.com",
    "databaseURL": "https://edubot-f2362.firebaseio.com",
    "projectId": "edubot-f2362",
    "storageBucket": "edubot-f2362.appspot.com",
    "messagingSenderId": "86712690656",
    "appId": "1:86712690656:web:811feadb6d97dcd3962d85",
    "measurementId": "G-TRPHQ88HGE"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# two decorators, same function
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            # flash("You need to login first")
            return redirect(url_for('login'))

    return wrap


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Edubot Home Page')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    unsuccessful = 'Credenciales Incorrectas'
    successful = 'Inicio de Sesion Correcto'
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                login = auth.sign_in_with_email_and_password(form.email.data, form.password.data)
                session.clear()
                session['logged_in']=True
                return redirect(url_for('perfil'))
            except:
                return render_template('login1.html', us=unsuccessful, form=form)
        else:
            return render_template('login1.html', us=unsuccessful, form=form)

    return render_template('login1.html', the_title='Login', form=form)

@app.route('/signin',  methods=['GET', 'POST'])
def signin():
    unsuccessful = 'Error en registro'
    successful = 'Se Registro Correctamente'
    form = SiginForm(request.form)
    if request.method=='POST':
        if form.validate():
            try:
                user = auth.create_user_with_email_and_password(form.email.data, form.password.data)
                auth.send_email_verification(user['idToken'])
                return render_template('signin1.html', s=successful, form=form)
            except:
                return render_template('signin1.html', us=unsuccessful, form=form)
        else:
            return render_template('signin1.html', us=unsuccessful, form=form)
    return render_template('signin1.html', the_title='Registrate', form=form)

@app.route('/juego/<int:i>')
def juego(i):
    return render_template('juego_base.html', game_title=game_dic[i]["game_title"], game_competence=game_dic[i]["game_competence"], game_description=game_dic[i]["game_description"], game_image=game_dic[i]["game_image"] )

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', the_title='Juego Líneas')
    
@app.route('/ranking')
@login_required
def ranking():
    return render_template('ranking.html', rank_dic=rank_dic)
    
@app.route('/game_lines')
def game_lines():
    return render_template('game_lines.html', the_title='Juego Líneas')

@app.route('/juegos')
def juegos():
    return render_template('search.html', the_title='Búsqueda de Juegos')
    
@app.route('/index2')
def juegos2():
    return render_template('index2.html', the_title='Búsqueda de Juegos')

@app.route('/contacto')
def contacto():
    return render_template('contact_us.html', the_title='Contáctanos')

@app.route('/formplayer', methods=['GET', 'POST'])
def formplayer():
    unsuccessful = 'Error en registro'
    successful = 'Se Registro Correctamente'
    if request.method=='POST':
        name = request.form['name_player']
        age = request.form['age_player']
        level = request.form['level_player']
        school = request.form['school_player']

        post = {
            "name": name,
            "age": age,
            "level": level,
            "school":school
        }

        try:
            db.child("Player").push(post)
            return render_template('forms/jugador.html', s=successful)

        except:
            return render_template('forms/jugador.html', us=unsuccessful)

    return render_template('forms/jugador.html', the_title='Formulario Jugador')

@app.route('/formschool')
@login_required
def formpschool():
    return render_template('forms/signin_school.html', the_title='Formulario Escuela')

@app.route('/formtutor')
@login_required
def formtutor():
    return render_template('forms/tutor.html', the_title='Formulario del Tutor')

@app.route('/filters')
def filters():
    return render_template('filters.html', the_title='Filtro para Juegos')




app.register_blueprint(edubot)

if __name__ == '__main__':
    app.run(debug= True)

