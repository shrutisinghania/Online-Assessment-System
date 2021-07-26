#!C:\Python27\python.exe
import MySQLdb
import cgi
import os
import Cookie
print("Content-type: text/html")
print

if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	try:
		dat=c['mou'].value
	except KeyError:
		print "The cookie was not set or has expired<br>"
db = MySQLdb.connect("localhost","root","","online_assesment" )
cursor=db.cursor()
data=cgi.FieldStorage()
given1=(data.getvalue('1'))
given2=(data.getvalue('2'))
given3=(data.getvalue('3'))
given4=(data.getvalue('4'))
given5=(data.getvalue('5'))
given6=(data.getvalue('6'))
given7=(data.getvalue('7'))
given8=(data.getvalue('8'))
given9=(data.getvalue('9'))
given10=(data.getvalue('10'))
ts= int(given1) + int(given2) + int(given3) + int(given4) + int(given5) + int(given6) + int(given7) + int(given8) + int(given9) + int(given10)
sql="insert into exam2(email,1given,2given,3given,4given,5given,6given,7given,8given,9given,10given,finalscore) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(dat,given1,given2,given3,given4,given5,given6,given7,given8,given9,given10,ts)
try:
	cursor.execute(sql)
	db.commit()
	print('<html>')
	print('<body>')
	print('<h1>Successfully Exam Given</h1>')
	print('<h2>Your Score is %s out of 100</h2>'%ts)
	print('<a href="login2_form.html">Login Again</a><br>')
	print('</body>')
	print('</html>')
except:
	db.rollback()
	print( '''<html>
	<body>
	<h2>Exam Already Given</h2>
	</body>
	</html>''' )
db.close()