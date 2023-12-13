from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'shop',
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    email = request.form['email']
    password = request.form['password']

    login_query = "SELECT email, password FROM users WHERE email = %s AND password = %s"
    data = (email, password)

    cursor.execute(login_query, data)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        # Store user details in session for future use
        user_id, user_name, user_surname, user_email = result
        return render_template('users.html', user_id=user_id, user_name=user_name, user_surname=user_surname, user_email=user_email)
    else:
        return "Login failed. Please check your email and password."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)
