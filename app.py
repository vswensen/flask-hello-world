from flask import Flask
import psycopg2

app = Flask(__name__)

DB_URL = "postgres://hello_db_v7zu_user:rgfQsrIjEEiwTT4R8pT5wqvptRXq6erf@dpg-cg9mac64dad5p6s6as90-a/hello_db_v7zu"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(DB_URL)
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
