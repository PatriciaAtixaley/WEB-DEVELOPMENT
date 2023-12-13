from flask import Flask, render_template, request
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
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        name = request.form['uname']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']

        check_email_query = "SELECT id FROM users WHERE email = %s"
        cursor.execute(check_email_query, (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            conn.close()
            return "Registration failed. Email already exists."

        insert_query = "INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
        data = (name, surname, email, password)
        cursor.execute(insert_query, data)

        conn.commit()
        cursor.close()
        conn.close()

        return "Registration successful!"

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)
