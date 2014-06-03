from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
def index():
	user = {
		'nickname' : 'Steve'
	}
	posts = [
		{
			'author' : { 'nickname' : 'John' },
			'body' : 'Beautiful day today!'
		},
		{
			'author' : { 'nickname' : 'Susan' },
			'body' : 'Another beautiful day!'
		}
	]
	return render_template("index.html",
		title = 'Home',
		user = user,
		posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/')

	return render_template('login.html',
		title = 'Sign In',
		form = form)