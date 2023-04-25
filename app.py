from flask import Flask, render_template, redirect, request, url_for, session, send_file
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import re
import secrets
import MySQLdb.cursors
from passlib.hash import sha256_crypt
from cryptography.fernet import Fernet


key = Fernet.generate_key()
crypter = Fernet(key)

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Anupam'
app.config['MYSQL_PASSWORD'] = '8955@Mysql'
app.config['MYSQL_DB'] = 'dog_show'

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method =='POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE name = %s ', (username,))
        account = cursor.fetchone()
        
        
        
        if account:
            pas = account['password']
            if(sha256_crypt.verify(password,pas)):
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['name']
                msg = 'Logged in successfully !'
                return render_template('main.html', username=username)
            
            else:
                msg = 'Incorrect username / password !'
            
        else:
            msg = 'Incorrect username / password !'
            
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        encpassword = sha256_crypt.encrypt(password)
        
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE name = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+/.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', (username, email, encpassword))
            mysql.connection.commit()
            msg = 'You have successfully reigstered !'
        
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    
    return render_template('register.html', msg=msg)

@app.route('/main', methods=['GET','POST'])
def main():
    msg = ''
    if request.method == 'POST' and 'owner_name' in request.form and 'mobile' in request.form and 'dog_name' in request.form and 'dog_breed' in request.form:
        owner_name = request.form['owner_name']
        mobile = request.form['mobile']
        dog_name = request.form['dog_name']
        dog_breed = request.form['dog_breed']
        dog_image = request.files['dog_image']
        
        # filename = secure_filename(dog_image.filename)
        # mimetype = dog_image.mimetype
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM register WHERE mobile = %s', (mobile,))
        dog = cursor.fetchone()
        
        if dog:
            msg = 'Dog already registered!'
        elif not owner_name or not mobile or not dog_name or not dog_breed:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO register VALUES(NULL, %s, %s, %s, %s, %s)', (owner_name, mobile, dog_name, dog_breed, dog_image))
            mysql.connection.commit()
            msg = 'You have successfully registered the dog!'
            
        return render_template('main.html',msg=msg)
            
        # return send_file('D:/Projects/College Minor Project/Python Image Classifier Project/alexnet_uploaded-images.txt', mimetype='text/plain')
    
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    
    return render_template('main.html',msg=msg)


@app.route('/about')
def about():
    
    return render_template('about.html')


@app.route('/team')
def team():
    
    return render_template('team.html')


@app.route('/result', methods=['GET','POST'])
def result():
    
    sql = ('SELECT * FROM register ORDER BY id DESC LIMIT 1')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    
    allDogs = cursor.fetchall()
    
    return render_template('result.html', allDogs=allDogs)




@app.route('/text')
def text():
    return send_file('D:/Projects/College Minor Project/Python Image Classifier Project/alexnet_uploaded-images.txt', mimetype='text/plain')
    # return send_file('path/to/your/file.txt', mimetype='text/plain')

if __name__=="__main__":
    app.run(debug=True, port=9000)