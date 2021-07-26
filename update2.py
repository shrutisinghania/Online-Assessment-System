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
        id=c['mou'].value
        print "Email Id: "+id+"<br>"
    except KeyError:
        print "The cookie was not set or has expired<br>"
db = MySQLdb.connect("localhost","root","","online_assesment" )
cur=db.cursor()
data=cgi.FieldStorage()
name=data.getvalue('a')
clg=data.getvalue('c')
password=data.getvalue('d')
cur.execute("update registration set name='"+name+"',college='"+clg+"',password='"+password+"' where email='"+id+"'")
db.commit()
print
print('''<html>
<head>
<title>update here</title>
</head>
<body>
<h2>updated</h2>
<a href="login2_form.html">login here</a>
</body>
</html>''')
