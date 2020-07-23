import pandas as pd
import os
import sqlite3

##### PART 2, MAKING AND POPULATING A DATABASE #####

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

con = sqlite3.connect(DB_FILEPATH)

df = pd.read_csv("buddymove_holidayiq.csv")
df.columns = ['UserId', 'Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
df.to_sql('review', con=con, if_exists='replace')

con.row_factory = sqlite3.Row

cursor = con.cursor()

query1 = "SELECT count(*) as total FROM review"
result1 = cursor.execute(query1).fetchone()
print('--------------------------------------------')
print(f"There are {result1['total']} rows")
print('--------------------------------------------')

query2 = """
            SELECT COUNT (UserId) as total
            FROM review
            WHERE Nature>99 AND Shopping>99
        """
result2 = cursor.execute(query2).fetchone()
print('--------------------------------------------')
print(f"There are {result2['total']} rows")
print('--------------------------------------------')
