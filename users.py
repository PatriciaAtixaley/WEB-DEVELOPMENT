from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'shop',
}

@app.route('/all_users')
def all_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Retrieve all users from the database
    get_all_users_query = "SELECT id, name, surname, email FROM users"
    cursor.execute(get_all_users_query)
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('all_users.html', users=users)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)