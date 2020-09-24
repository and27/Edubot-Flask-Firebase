from flask import Flask, render_template, request, redirect, session, url_for
from functools import wraps
from rank_dic import rank_dic 
from game_dic import game_dic
from views.api_player import edubot
import pyrebase



app = Flask(__name__)

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
db = firebase.database()



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

@app.route('/login', methods=['GET', 'POST'])
def login():
    unsuccessful = 'Credenciales Incorrectas'
    successful = 'Inicio de Sesion Correcto'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['passd']
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            #auth.send_email_verification(login['idToken'])
            return redirect(url_for('perfil'))
        except:
            return render_template('login.html', us=unsuccessful)

    return render_template('login.html', the_title='Login')

@app.route('/signin',  methods=['GET', 'POST'])
def signin():
    unsuccessful = 'Error en registro'
    successful = 'Se Registro Correctamente'
    if request.method=='POST':
        email = request.form['mail']
        password = request.form['pass']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken'])
            return render_template('signin.html', s=successful)
        except:
            return render_template('signin.html', us=unsuccessful)

    return render_template('signin.html', the_title='Registrate')

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

@app.route('/filters')
def filters():
    return render_template('filters.html', the_title='Filtro para Juegos')




app.register_blueprint(edubot)

if __name__ == '__main__':
    app.run(debug= True)

