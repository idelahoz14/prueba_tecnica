from db import get_db
from flask import Flask, app, request
from flask.helpers import flash, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask import jsonify

app = Flask(__name__)

#settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = get_db().cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()

    return render_template('index.html', users=data)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        firstName = request.form['firstName']
        middleName = request.form['middleName']
        lastName = request.form['lastName']
        email = request.form['email']
        code = request.form['zipCode']

        #Sqlite consult
        cur = get_db().cursor()
        cur.execute('INSERT INTO  users (firstName, middleName, lastName, email, zipCode) VALUES (?, ?, ?, ?, ?)',
        (firstName, middleName, lastName, email, code))
        get_db().commit()
        flash('Contact added suscesfully')
        data = jsonify(firstName=firstName, middleName=middleName, lastName=lastName, email=email, zipCode=code)
        return data

@app.route('/edit_user/<int:id>')
def get_user(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM users WHERE id = {0}'.format(id))
    data = cur.fetchall()

    return render_template('get_user.html', user = data[0])

@app.route('/delete_user/<int:id>')
def delete_user(id):
    cur = get_db().cursor()
    cur.execute('DELETE FROM users WHERE id = {0}'.format(id))
    get_db().commit()
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
