import sqlite3

conn = sqlite3.connect("web.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM Itmo")
print(cursor.fetchall())
cursor.close()
conn.close()
