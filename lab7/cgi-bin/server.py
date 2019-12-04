#!/usr/bin/python
import sqlite3

conn = sqlite3.connect("web.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM Itmo")
data = cursor.fetchall()
cursor.close()
conn.close()
#print(data[0][0])

print("Content-type: text/html")
print()

for record in data:
    print("""<form action="/cgi-bin/form.py">
        <input type="submit" name="Button" value={}>
    </form>""".format(record[0]))

