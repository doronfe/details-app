import os,sys
from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
import psycopg2
from src.details.libs import connectionForm

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
conn = psycopg2.connect(host="postgres-database", dbname="users-details", user="postgres", password="postgres")
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS details (name VARCHAR(255), email VARCHAR(255));""")
add_user= ("INSERT INTO details (name, email) VALUES (%s, %s)")
app.config['SECRET_KEY'] = '!!5S0m#wh$tVERYL0nGQWERTYpa$$W0d'
#db = SQLAlchemy(app)

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