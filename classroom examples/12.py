import xlrd
book = xlrd.open_workbook("example.xls")
print(book.nsheets)			# print number of sheets
print(book.sheet_names())		# print sheet names
first_sheet = book.sheet_by_index(0)    # get the first worksheet
print (first_sheet.row_values(0))		# read a row
cell = first_sheet.cell(0,0)		# read a cell
print(cell.value)

