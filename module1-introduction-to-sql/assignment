import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
#print("CONNECTION:", connection)

cursor = connection.cursor()
#print("CURSOR", cursor)

query1 = "SELECT count(distinct character_id) as total FROM charactercreator_character"
result1 = cursor.execute(query1).fetchall()
print('--------------------------------------------')
print(f"There are {result1[0]['total']} characters in total")
print('--------------------------------------------')

query2_a ="SELECT count(distinct character_ptr_id) as total FROM charactercreator_cleric"
result2_a = cursor.execute(query2_a).fetchall()
print(f"There are {result2_a[0]['total']} clerics")

query2_b ="SELECT count(distinct character_ptr_id) as total FROM charactercreator_fighter"
result2_b = cursor.execute(query2_b).fetchall()
print(f"There are {result2_b[0]['total']} fighters" )

query2_c ="SELECT count(distinct character_ptr_id) as total FROM charactercreator_mage"
result2_c = cursor.execute(query2_c).fetchall()
print(f"There are {result2_c[0]['total']} mages")

query2_d ="SELECT count(distinct mage_ptr_id) as total FROM charactercreator_necromancer"
result2_d = cursor.execute(query2_d).fetchall()
print(f"There are {result2_d[0]['total']} necromancers")

query2_e ="SELECT count(distinct character_ptr_id) as total FROM charactercreator_thief"
result2_e = cursor.execute(query2_e).fetchall()
print(f"There are {result2_e[0]['total']} thieves")
print('--------------------------------------------')

query3 = "SELECT COUNT(DISTINCT item_id) as total FROM charactercreator_character_inventory"
result3 = cursor.execute(query3).fetchall()
print(f"There are {result3[0]['total']} items")
print('--------------------------------------------')

query4 = "SELECT count ( DISTINCT item_id) as total FROM armory_item where item_id in (SELECT item_ptr_id FROM armory_weapon)"
result4 = cursor.execute(query4).fetchall()
print(f"There are {result4[0]['total']} weapons out of items")
print('--------------------------------------------')

query5 = "SELECT count ( DISTINCT item_id) as total FROM armory_item where item_id not in (SELECT item_ptr_id FROM armory_weapon)"
result5 = cursor.execute(query5).fetchall()
print(f"There are {result5[0]['total']} items that are not weapons")
print('--------------------------------------------')

query6 = "SELECT character_id as ch, count(item_id) nb_item FROM charactercreator_character_inventory group by character_id"
result6 = cursor.execute(query6).fetchmany(20)
print("Here are the 20 first characters with the number of item they have")
for row in result6:
    print(row["ch"], row["nb_item"])
print('============================================')

query7 = """
SELECT iv.character_id, ch.name, count(iv.item_id) AS weapon FROM charactercreator_character_inventory AS iv 
JOIN charactercreator_character as ch ON iv.character_id = ch.character_id 
JOIN armory_weapon as wea ON iv.item_id = wea.item_ptr_id 
GROUP BY iv.character_id;
"""
result7 = cursor.execute(query7).fetchmany(20)
print("Here are the first 20 charachter with the number of weapons they have")
for row in result7:
    print(row["name"], row["weapon"])
print('============================================')

query8 = """    
         SELECT AVG(items) 
         FROM(SELECT character_id, Count(character_id) as items 
	          FROM charactercreator_character_inventory
	          GROUP by character_id)
"""
result8 = cursor.execute(query8).fetchone()
print(f"On average, each character has {result8[0]} items")
print('============================================')

query9 = """
         SELECT AVG(weapon_) AS average
         FROM (SELECT character, COUNT(weapons) as weapon_
               FROM (SELECT character_id AS character, item_ptr_id as weapons
                     FROM charactercreator_character_inventory chara
                     LEFT JOIN armory_weapon weapon ON chara.item_id = weapon.item_ptr_id)
               GROUP BY character)
         """
result9 = cursor.execute(query9).fetchone()
print(f"On average, each character has {result9[0]} weapons")
print('============================================')
