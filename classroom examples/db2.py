import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
# insert some data
cursor.execute("INSERT INTO books VALUES (1, 'Wings of Fire', 'Abdul Kalam')")
# save data to database
print("Record inserted")
conn.commit()
conn.close()
