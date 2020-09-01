from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Edubot Home Page')

@app.route('/login')
def login():
    return render_template('login.html', the_title='Login')

@app.route('/signin')
def signin():
    return render_template('signin.html', the_title='Registrate')

@app.route('/juego')
def juego():
    return render_template('juego.html', the_title='Juego')

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

if __name__ == '__main__':
    app.run(debug=True)
