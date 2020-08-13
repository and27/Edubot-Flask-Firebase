from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Edubot Home Page')

@app.route('/login.html')
def login():
    return render_template('login.html', the_title='Login')

@app.route('/signin.html')
def signin():
    return render_template('signin.html', the_title='Registrate')

@app.route('/juego.html')
def juego():
    return render_template('juego.html', the_title='Juego')

@app.route('/statistics.html')
def statistics():
    return render_template('statistics.html', the_title='Estadisticas')

if __name__ == '__main__':
    app.run(debug=True)
