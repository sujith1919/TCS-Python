#create table
import sqlite3
conn = sqlite3.connect("marks.db")
cursor = conn.cursor()
# create a table
sql="""
CREATE TABLE marks2(
rowid integer primary key autoincrement,
student text,
maths integer,
english integer,
science integer
 ) 
"""
cursor.execute(sql)
print("Table Created")

#get data from csv file
markslist=[]
f=open("marks.csv","r")
f.readline()
for line in f:
	fields=line.strip().split(",")
	record=[]
	record.append(fields[0])
	for x in fields[1:]:
		record.append(int(x))
	markslist.append(tuple(record))
print(markslist)
f.close()
#insert into database
cursor.executemany("INSERT INTO marks2 (student,maths,english,science) VALUES(?,?,?,?)", markslist)
print("{} books inserted".format(cursor.rowcount))
conn.commit()
#verify by printing from database

for row in cursor.execute("select * from marks2"):
	print(row)
	
conn.close()