import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
# create a table
sql="""
CREATE TABLE books(
id int,
title text,
author text
 ) 
"""
cursor.execute(sql)
print("Table Created")
conn.close()