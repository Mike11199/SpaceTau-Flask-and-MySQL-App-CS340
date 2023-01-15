from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

USER_NAME = os.getenv("USER_NAME")
PASSWORD_LAST_4_ONID = os.getenv("ONID_LAST_4")


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = USER_NAME
app.config['MYSQL_PASSWORD'] = PASSWORD_LAST_4_ONID #last 4 of onid
app.config['MYSQL_DB'] = USER_NAME
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def root():
    query = "SELECT * FROM diagnostic;"
    query1 = 'DROP TABLE IF EXISTS diagnostic;'
    query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);'
    query3 = 'INSERT INTO diagnostic (text) VALUES ("testing for final project!!")'
    query4 = 'SELECT * FROM diagnostic;'
    cur = mysql.connection.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    results = cur.fetchall()

    return "<h1>MySQL Results" + str(results[0])


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted; changed to 6574 per tutorial video
    app.run(port=6717, debug=True)