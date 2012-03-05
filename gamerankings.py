import os
from urllib2 import urlopen
from urlparse import urljoin,urlsplit
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer

for i in range(85):
url="http://www.gamerankings.com/browse.html?page=" + i
a=urlopen(url).read()
b=SoupStrainer("table")
soup=bs(a,parseOnlyThese=b)
info=soup.find("table")
#print str(info)
ab=info.ul.li
print str(ab)
while (ab):
      name=str(ab.a.findAll("span")[1].h3.contents[0])
      rating=str(ab.a.span.contents[0])
      type=str(ab.a.findAll("span")[1].span.contents[0])
      print name , rating  , type
      ab=ab.nextSibling.nextSibling
