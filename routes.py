from flask import Flask, render_template, request, redirect, session
from game_dic import game_dic
import pyrebase



app = Flask(__name__)

firebaseConfig = {
  "apiKey": "AIzaSyA879qkoq7PGHdL3YYhO4LaW-OHmxuLHWY",
  "authDomain": "webpage-15b17.firebaseapp.com",
  "databaseURL": "https://webpage-15b17.firebaseio.com",
  "projectId": "webpage-15b17",
  "storageBucket": "webpage-15b17.appspot.com",
  "messagingSenderId": "846775345641",
  "appId": "1:846775345641:web:5298dd967cd538b3d2ab78",
  "measurementId": "G-E6XE42VMWC"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# two decorators, same function
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
            return render_template('login.html', s=successful)
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
def perfil():
    return render_template('statistics.html', the_title='Juego Líneas')
	
@app.route('/ranking')
def ranking():
    return render_template('ranking.html', the_title='Juego Líneas')
	
@app.route('/game_lines')
def game_lines():
    return render_template('game_lines.html', the_title='Juego Líneas')

@app.route('/juegos')
def juegos():
    return render_template('search.html', the_title='Búsqueda de Juegos')
	
@app.route('/index2')
def juegos2():
    return render_template('index2.html', the_title='Búsqueda de Juegos')


if __name__ == '__main__':
    app.run(debug= True)

