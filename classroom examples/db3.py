import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
# insert multiple records using the more secure "?" method
mybooks = [(2, 'My Experiments with Truth', 'M K Gandhi'),
          (3, 'Discovery of India', 'J Nehru'),
		  (4, 'My Experiments with Food', 'Ramesh S')]
cursor.executemany("INSERT INTO books VALUES (?,?,?)", mybooks)
print("{} books inserted".format(cursor.rowcount))
conn.commit()
conn.close()
