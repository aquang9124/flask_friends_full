from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
mysql = MySQLConnector('mydb')
app = Flask(__name__)
app.secret_key = 'lakdfJee54.2ThisISTheSecretKey'

@app.route('/')
def index():
	friends = mysql.fetch("SELECT * FROM users")
	return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO users (first_name, last_name, occupation, email, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'], request.form['email'])
	mysql.run_mysql_query(query)
	return redirect('/')
@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
	friend = mysql.fetch("SELECT * from users where id = %s" % str(friend_id))
	return render_template('edit.html', friend=friend)
@app.route('/friends/update/<friend_id>', methods=['POST'])
def update(friend_id):
	query = "UPDATE users SET first_name = '{}', last_name = '{}', occupation='{}', email='{}' WHERE id = '{}'".format(request.form['first_name'], request.form['last_name'], request.form['occupation'], request.form['email'], friend_id)
	mysql.run_mysql_query(query)
	return redirect('/')
@app.route('/friends/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):
	query = "DELETE FROM users WHERE id = '{}'".format(friend_id)
	mysql.run_mysql_query(query)
	return redirect('/')
app.run(debug=True)