#!C:\Python27\python.exe
import MySQLdb
import cgi
import os
import Cookie
print("Content-type: text/html")
print
print """
<html>
<body>
<h1></h1>
"""

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data=c['mou'].value
        print "Email Id: "+data+"<br>"
    except KeyError:
        print "The cookie was not set or has expired<br>"
db = MySQLdb.connect("localhost","root","","online_assesment" )
cur=db.cursor()
cur.execute("select * from registration where email='"+data+"'")
results=cur.fetchall()
for row in results:
	name=row[0]
	clg=row[1]
	password=row[3]
print """
<form action="update2.py">
enter name to be update(if needed):<input type="text" name="a" value='""" + name + """'><br>
enter college to be update(if needed):<input type="text" name="c" value='""" + clg + """'><br>
enter password to be update(if needed):<input type="text" name="d" value='""" + password + """'><br><br>
<input type="submit" name="submit" value="update">
</form>
</body>
</html>

"""
