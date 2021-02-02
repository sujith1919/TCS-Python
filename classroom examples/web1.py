#how to use bottle
import os
import sqlite3
from bottle import route, run, request, template
@route('/')
def hello():
    return "Hey I am bottle here how are you doing?"
@route('/contact')
def contact():
    return "Hey you can reach me on rsannareddy@gmail.com?"
@route('/env')
def abcd():
	output='<table border=1>'
	for x,y in os.environ.items():
		output=output +"<tr><td>"+ x +"</td><td>"+ y + "</td></tr>"
	return output + "</table>"
@route('/wish/<name>')
def wish(name):
	return "hello " + name
@route('/books')
def books():
	conn = sqlite3.connect("mydatabase.db")
	cursor = conn.cursor()
	output='<table border=1>'
	tablerow="<tr><td>{}</td><td>{}</td></tr>"
	sql = "SELECT * FROM books"
	
	for id,bookname,author in cursor.execute(sql):
		 output+=tablerow.format(bookname,author)
	output+="</table>"
	
	conn.close()
	return output

@route("/books/id/<id>")
def bookid(id):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    output='<table border=1>'
    tablerow="<tr><td>{}</td><td>{}</td></tr>"
    sql = "SELECT * FROM books where id={}".format(id)
    for id,bookname,author in cursor.execute(sql):
        output+=tablerow.format(bookname,author)
    output+="</table>"
    conn.close()
    return output

@route('/add')
def showform():
	return """
<html>
<form method=post action="http://localhost:8080/addbook">
<input type=text name=id>Id<br>
<input type=text name=bookname>Book name<br>
<input type=text name=author>Author<br>
<input type=submit>
</form>
</html>

	"""
@route('/addbook', method='POST')
def login():
	conn = sqlite3.connect("mydatabase.db")
	cursor = conn.cursor()
	id=request.forms.get('id')
	bookname=request.forms.get('bookname')
	author=request.forms.get('author')
	sql="INSERT INTO books VALUES ({}, '{}','{}')".format(id,bookname,author)
	cursor.execute(sql)
	conn.commit()
	conn.close()
	return "<a href=/books>Book List</a>"



run(host='localhost', port=8080, debug=True)
