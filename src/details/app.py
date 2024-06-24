import os,sys
from flask import Flask, render_template, request, redirect
from psycopg2 import connect, OperationalError
from src.details.libs import connectionForm
from time import sleep

app = Flask(__name__)

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    try:
        conn = connect(host="postgres-database", dbname="users-details", user="postgres", password="postgres")
        print("Connected to the database successfully!")
        break
    except OperationalError as e:
        attempts += 1
        print(f"Attempt {attempts} failed with error: {e}")
        print(f"Waiting for 5 seconds before retrying...")
        sleep(5)
        if attempts == max_attempts:
            print("Could not connect to the database after several attempts.")




cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS details (name VARCHAR(255), email VARCHAR(255));""")
add_user= ("INSERT INTO details (name, email) VALUES (%s, %s)")
app.config['SECRET_KEY'] = '!!5S0m#wh$tVERYL0nGQWERTYpa$$W0d'

@app.route('/',methods=['GET', 'POST'])
def index():
    form = connectionForm()
    if request.method == 'POST':
        contact_info = {'email': request.form.get('Email'), 'name': request.form.get('Name')}
        cur.execute(add_user, (contact_info['name'],contact_info['email']))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/')
    return render_template('index.html', form=form)