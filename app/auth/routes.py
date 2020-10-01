from flask import render_template,  Flask, request, jsonify, session, redirect, url_for
from firebase_admin import credentials, firestore, initialize_app
from responses.responses import bad_request, response
from . import auth_b
import os
from os.path import dirname
from form import SiginForm, LoginForm
dir = dirname(dirname(__file__))

@auth_b.route('/login', methods=['GET', 'POST'])
def login():
	os.chdir(dir)
	from app import auth
	unsuccessful = 'Credenciales incorrectas'
	successful = 'Inicio de Sesión Correcto'
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate():
			try:
				login = auth.sign_in_with_email_and_password(form.email.data, form.password.data)
				session.clear()
				session['logged_in']=True
				return redirect(url_for('perfil'))
			except:
				return render_template('login.html', us=unsuccessful, form=form)
		else:
			return render_template('login.html', us=unsuccessful, form=form)
			
	return render_template('login.html', the_title='Login', form=form)

@auth_b.route('/register',  methods=['GET', 'POST'])
def register():
	os.chdir(dir)
	from app import auth
	unsuccessful = 'Error en registro'
	successful = 'Se Registro Correctamente'
	form = SiginForm(request.form)
	if request.method=='POST':
		if form.validate():
			try:
				user = auth.create_user_with_email_and_password(form.email.data, form.password.data)
				auth.send_email_verification(user['idToken'])
				return render_template('register.html', s=successful, form=form)
			except:
				return render_template('register.html', us=unsuccessful, form=form)
		else:
			return render_template('register.html', us=unsuccessful, form=form)
	return render_template('register.html', the_title='Registrate', form=form)


if __name__ == "__main__":
	pass