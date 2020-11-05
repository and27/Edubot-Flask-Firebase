from flask import Flask, render_template, request, redirect, session, url_for
from functools import wraps
from rank_dic import rank_dic 
from game_dic import game_dic
from game2_dic import game2_dic
#from views.api_player import edubot
from api.api_school import edubot
import pyrebase
from form import SiginForm, LoginForm
import os
from auth import auth_b 

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

player={
    "name":"Pepito Pérez",
    "school":"Unidad Educativa Ibarra",
    "age":"7 años",
    "grade":"Quinto de básica",
    "nickname":"pep123",
    "points":120,
    "llaves":5,
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
            return redirect(url_for('auth.login'))

    return wrap


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Edubot Home Page', largefooter=True)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@app.route('/juego/<int:i>')
def juego(i):
    return render_template('juego_base.html', game_title=game_dic[i]["game_title"], game_competence=game_dic[i]["game_competence"], game_description=game_dic[i]["game_description"], game_image=game_dic[i]["game_image"] )

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil_player_base.html', the_title='Juego Líneas', player=player)

@app.route('/perfil_player')
@login_required
def perfil_player():
    return render_template('perfil_player_base.html', the_title='Juego Líneas', player=player)

@app.route('/perfil_tutor')
#@login_required
def perfil_tutor():
    return render_template('perfil_tutor_base.html', the_title='Juego Líneas', player=player, users=True)
     
@app.route('/ranking')
@login_required
def ranking():
    return render_template('ranking.html', rank_dic=rank_dic)
    
@app.route('/game_lines')
def game_lines():
    return render_template('game_lines.html', the_title='Juego Líneas')

@app.route('/juegos')
def juegos():
    return render_template('filters_base.html', the_title='Búsqueda de Juegos',  game2_dic=game2_dic)
    
@app.route('/juegospag')
def juegospag():
    return render_template('pagination_games.html', the_title='Búsqueda de Juegos',  game2_dic=game2_dic)
    
@app.route('/index2')
def juegos2():
    return render_template('index2.html', the_title='Búsqueda de Juegos')

@app.route('/contacto')
def contacto():
    return render_template('contact_us.html', the_title='Contáctanos')

@app.route('/FQAs')
def fqas():
    return render_template('FQAs.html', the_title='FQAs')

@app.route('/acerca')
def acerca():
    return render_template('about_us.html', the_title='Acerca de Nosotros')

@app.route('/team')
def team():
    return render_template('our_team.html', the_title='Nuestro Equipo')

@app.route('/animations')
def animations():
    return render_template('animations.html', the_title='Animations', largefooter=True)

@app.route('/cards')
def cards():
    return render_template('filters_base.html', game2_dic=game2_dic)


@app.route('/store')
def store():
    return render_template('store.html', the_title='Tienda')

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





app.register_blueprint(edubot)
app.register_blueprint(auth_b)

if __name__ == '__main__':
    app.run(debug= True)

