import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
print("listing of all the records in the table:")
for row in cursor.execute("SELECT * FROM books"):
    print(row[0],row[1],row[2])
 
print("Results")
sql = "SELECT * FROM books"
cursor.execute(sql)
for id,bookname,author in cursor.fetchall():
	print( "The book {} was written by {}".format(bookname,author))
	
sql = "SELECT * FROM books where id = 2"
cursor.execute(sql)

print(cursor.fetchone())

sql = "SELECT count(*) FROM books"
cursor.execute(sql)
print(cursor.fetchone())

conn.close()
