import sqlite3
 
conn = sqlite3.connect("web.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Itmo
                  (Year TEXT, Description TEXT)
               """)

cursor.close()
conn.close()
