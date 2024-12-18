from flask import Blueprint, request, render_template, redirect, url_for, session
from services.db_service import get_database_connection
import bcrypt

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_database_connection()
        user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session['user_name'] = user['name']
            return redirect(url_for('auth.menu'))

        return "Invalid credentials. Please try again.", 401

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        db = get_database_connection()
        try:
            db.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                       (name, email, hashed_password.decode('utf-8')))
            db.commit()
            return render_template('registration_success.html', name=name)
        except:
            return render_template('register.html', error="Email already registered.")

    return render_template('register.html')


@auth_bp.route('/menu')
def menu():
    user_name = session.get('user_name', 'User')
    return render_template('menu.html', user_name=user_name)


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
