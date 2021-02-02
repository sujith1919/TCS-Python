import sqlite3
import etl
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
# create a table
sql="""
CREATE TABLE marks(
name text,
maths text,
science text,
english text
 ) 
"""
cursor.execute(sql)
print("Table Created")

etl.csv2xls("marks.csv","marks-dump.xls")
etl.csv2db("marks.csv",cursor,"marks",conn)
etl.db2xls(cursor,"marks","marks-dump-from-db.xls")
etl.db2csv(cursor,"marks","marks-dump-from-db.csv")
etl.xls2csv("marks-dump-from-db.xls","marks-dump-from-xl.csv")
conn.close()

