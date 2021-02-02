import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
sql = """
UPDATE books 
SET author = 'Jawaharlal Nehru' 
WHERE id = 3
"""
cursor.execute(sql)
print("{} record(s) updated".format(cursor.rowcount))
conn.commit()
conn.close()