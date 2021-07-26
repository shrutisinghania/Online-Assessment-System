#!C:\Python27\python.exe
import MySQLdb
import cgi
import Cookie
# Open database connection
db = MySQLdb.connect("localhost","root","","online_assesment" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
data=cgi.FieldStorage()
a=data.getvalue('e1')
b=data.getvalue('p1')
# Prepare SQL query to fetch a record into the database.
sql = "select email,password from registration where email='"+a+"' AND password='"+b+"'"
try:
	# Execute the SQL command
	if(cursor.execute(sql)):
		# Commit your changes in the database
		db.commit()
		c=Cookie.SimpleCookie()
		# assign a value
		c['mou']=a
		# set the xpires time
		c['mou']['expires']=24*60*60
		# print the header, starting with the cookie
		print c
		print("Content-type: text/html")
		print
		print('''<html>
<head>
<title>login here</title>
</head>
<body>
<h2>successfully login</h2>
<a href="edit2.py">edit profile</a><br><br>
<a href="c.html">C Exam</a><br><br>
<a href="java.html">Java Exam</a><br><br>
<a href="logout2.py">logout</a><br><br>
</body>
</html>''')
	else:
		# Commit your changes in the database
		db.commit()
		print("Content-type: text/html")
		print
		print("<html>")
		print("<body>")
		print("<h2>Login Failed</h2>")
		print("</body>")
		print("</html>")
except:
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()