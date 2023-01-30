import sqlite3

db = sqlite3.connect(r'C:\Users\oldri\Desktop\BRONCOPROJECT\ExoBronco-Avionics\Software\GroundStation\test.db')    
cursor = db.cursor()
cursor.execute("SELECT * FROM playlists") 
rows = cursor.fetchall() 
for row in rows: 
    print (row) 
db.close()