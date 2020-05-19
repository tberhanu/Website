from flask import Flask
from flask import make_response, redirect, abort, render_template
app = Flask(__name__)

@app.route('/')
def index():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	# import pdb;pdb.set_trace()
	return response
	# return '<h1>Hello Start Up!!!</h1>'

@app.route('/index/<name>')
def index_template(name):
	return render_template('index.html', name=name)

@app.route('/user')
def user_template():
	return render_template('user.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/registration')
def register():
	return render_template('registration.html')

@app.route('/sign_up')
def sign_up():
	return render_template('sign_up.html')

@app.route('/sign_in')
def sign_in():
	return render_template('sign_in.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500
# @app.route('/user/<name>')
# def user(name):
# 	if name == "tess":
# 		abort(404)
# 	return '<h1>Hello, %s!</h1>' % name

@app.route('/xxx')
def useronly():
	return 'Bad Request</h1>', 400

@app.route('/redirect')
def registration():
	# Redirecting to the Registration Page
	return redirect('https://www.google.com')

@app.route('/students')
def list_students():
	students = {"Henock", "Abebe", "Shewit", "James"}
	return render_template('user.html', students=students)

if __name__ == '__main__':
	app.run(debug=True)
