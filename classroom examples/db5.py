import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
sql = """
DELETE FROM books
WHERE id = 4
"""
cursor.execute(sql)
print("{} record(s) deleted".format(cursor.rowcount))
conn.commit()
conn.close()