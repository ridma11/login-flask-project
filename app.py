# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import test
from playsound import playsound

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ridmadb'

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('index2.html')
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

@app.route('/my-link1/',methods=['GET'])
def my_link3():
  return my_link(),my_link2()
def my_link():
  return 'Genarated original sample rate 44.1 kHz .'
def my_link2():
  return test.sound2()


@app.route('/my-link2/',methods=['GET'])
def my_link31():
  return my_link1(),my_link21()
def my_link1():
  return 'Genarated wav[0] is L channel, wav[1] is R.'
def my_link21():
  return test.sound3()


@app.route('/my-link3/',methods=['GET'])
def my_link32():
  return my_link2(),my_link22()
def my_link2():
  return 'Genarated sound amplitude halved; wav[1] amplitude remains the same'
def my_link22():
  return test.sound4()
  
@app.route('/my-link4/',methods=['GET'])
def my_link33():
  return my_link3(),my_link23()
def my_link3():
  return 'Genarated sound amplitude halved; wav[1] amplitude remains the same'
def my_link23():
  return test.sound5()

@app.route('/my-link5/',methods=['GET'])
def my_link34():
  return my_link4(),my_link24()
def my_link4():
  return 'Genarated since 5e3 is float'
def my_link24():
  return test.sound6()

@app.route('/my-link6/',methods=['GET'])
def my_link35():
  return my_link5(),my_link25()
def my_link5():
  return 'Genarated 5 seconds onwards, R channel only'
def my_link25():
  return test.sound7()

@app.route('/my-link7/',methods=['GET'])
def my_link36():
  return my_link5(),my_link26()
def my_link6():
  return 'Mix a 440Hz (middle A) sine wave to the L channel'
def my_link26():
  return test.sound10()
  
if __name__ == '__main__':
  app.run(debug=True)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
	
