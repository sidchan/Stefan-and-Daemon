import os
from urllib2 import urlopen
from urlparse import urljoin,urlsplit
from bs4 import BeautifulSoup as bs 

for i in range(85):
url="http://m.ign.com/games/reviews-editors-choice/p" + i
soup=bs(urlopen(url).read())
info=soup.find("ul")
ab=info.li
print str(ab)
while (ab):
      name=str(ab.a.findAll("span")[1].h3.contents[0])
      rating=str(ab.a.span.contents[0])
      type=str(ab.a.findAll("span")[1].span.contents[0])
      print name , rating  , type
      ab=ab.nextSibling.nextSibling
