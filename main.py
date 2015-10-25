import urllib
import urllib2
import re

url="http://warbandmain.taleworlds.com/handlerservers.ashx?type=list&gametype=wfas"

headers={
    "GET":"warbandmain.taleworlds.com/handlerservers.ashx?type=list&gametype=wfas",
    "Host":"warbandmain.taleworlds.com",
    "User-Agent":"Mozilla/4.0",
    }

req=urllib2.Request(url)
for key in headers:
    req.add_header(key,headers[key])
html = urllib2.urlopen(req).read()

#print html
ss = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}[^|]|\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}[^|]",html)
for i in ss:
    print i
