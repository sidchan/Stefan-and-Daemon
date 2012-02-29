import urllib2
from bs4 import BeautifulSoup as bs
import threading
import scoregrab

class Gamespot(threading.Thread):
    def __init__(self,url):
        self.url=url
        
    def run(self):
        page=urllib2.urlopen(self.url).read()
        parser=bs(page)
        a=parser.find("table",{"summary":"GameSpot's All Reviews"})
        game=a.tbody.tr
        while (game):
            title=str(game.th.a.contents[0])
            
            scorgrab.Gamespot()
            platform=a.tbody.td.span.contents[0]
            scoreline=a.find("td",{"class":"score"}) 