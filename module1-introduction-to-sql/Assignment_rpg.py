import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
import os 
os.listdir()
query ='SELECT * FROM charactercreator_character;'
curs = conn.cursor()
len(curs.execute(query).fetchall())