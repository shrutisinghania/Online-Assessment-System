#!C:\Python27\python.exe
# Import modules for CGI handling 
import MySQLdb
import cgi
print("Content-type: text/html")
print
print('<meta HTTP-EQUIV="REFRESH" content="0; url=login2_form.html">')
'''var cookies = document.cookie.split(";")
for (var i = 0; i < cookies.length; i++) {
	var cookie = cookies[i];
	var eqPos = cookie.indexOf("=");
	var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
	document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
}'''