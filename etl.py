import xlrd
import xlwt

def csv2xls(csvfile,xlfile):
    csv=open(csvfile,'r')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('First Sheet')
    for row,rowdata in enumerate(csv):
        for col,celldata in enumerate(rowdata.strip().split(",")):
            ws.write(row, col, celldata)
    csv.close()
    wb.save(xlfile)
    
def csv2db(csvfile,cursor,table,conn):
    csv=open(csvfile,'r')
    csv.readline() #skip the header line
    records=[]
    for line in csv:
        fields=line.strip().split(",")
        records.append(tuple(fields))
        query="INSERT INTO {} VALUES ({})".format(table,",".join(len(fields) * "?"))
        cursor.executemany(query, records)
    conn.commit()
    csv.close()
    
def db2xls(cursor,table,xlfile):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('First Sheet')
    query = "SELECT * FROM {}".format(table)
    for row,rowdata in enumerate(cursor.execute(query)):
        for col,celldata in enumerate(rowdata):
            ws.write(row, col, celldata)
    wb.save(xlfile)
    
def db2csv(cursor,table,csvfile):
    csv=open(csvfile,'w')
    query = "SELECT * FROM {}".format(table)
    for rowdata in cursor.execute(query):
        rowdata=map(str,rowdata) # convert all fields to strings
        csv.write(",".join(rowdata) + "\n")
    csv.close()
    
def xls2csv(xlfile,csvfile):
    csv=open(csvfile,'w')
    book = xlrd.open_workbook(xlfile)
    first_sheet = book.sheet_by_index(0)# get the first worksheet
    for rownum in range(first_sheet.nrows):
        row=first_sheet.row_values(rownum)
        csv.write(",".join(row) + "\n")
    csv.close()
