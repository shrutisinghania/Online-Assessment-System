#!C:\Python27\python.exe
import MySQLdb
import cgi
db= MySQLdb.connect("localhost","root","","online_assesment")
cursor=db.cursor()
data=cgi.FieldStorage()
a=data.getvalue('n1')
b=data.getvalue('c1')
c=data.getvalue('e1')
d=data.getvalue('p1')
e=data.getvalue('g1')
sql="insert into registration(name,college,email,password,gender) values('%s','%s','%s','%s','%s')"%(a,b,c,d,e)
try:
	cursor.execute(sql)
	db.commit()
	print("Content-type: text/html")
	print
	print('''<html>
	<head>
	<title>register here</title>
	</head>
	<body>
	<h2>success</h2>
	<a href="login2_form.html">login here</a>
	</body>
	</html>''')
except:
	print
	print('''<html>
	<body>
	<h2>Email Already Registered</h2>
	<a href="login2_form.html">Login Here</a>
	</body>
	</html>''')
	db.rollback()
db.close()