#read from table marks2
#write into file marks2.xls

import sqlite3
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('Marks')

conn = sqlite3.connect("c://users//tring//desktop//synechron2//marks.db")
cursor = conn.cursor()
j = cursor.execute("SELECT * FROM marks2")

#writing the header row
for col,data in enumerate(j.description):
    ws.write(0,col,data[0])

#writing data
for row,data in enumerate(j):
    for col,celldata in enumerate(data):
        ws.write(row+1,col,celldata)
wb.save('marks.xls')
    

conn.close()
