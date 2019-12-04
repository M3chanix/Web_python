#!/usr/bin/python
import cgi
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


form = cgi.FieldStorage()
value = form.getvalue("Button")

print("Content-type: text/html; charset=utf-8")
print()
print("<p>{}</p>".format(data_dict[value]))

