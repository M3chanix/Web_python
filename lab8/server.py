#!/usr/bin/python
import flask
import sqlite3

conn = sqlite3.connect("web.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM Itmo")
data = cursor.fetchall()
cursor.close()
conn.close()

data_dict = {}

for i in data:
    data_dict[i[0]]=i[1]

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Itmo/')
@app.route('/Itmo/<year>')
def render(year=None, data_dict=data_dict):
    text = data_dict[year]
    return flask.render_template('page.html', text=text)

if __name__ == '__main__':
    app.run()  

