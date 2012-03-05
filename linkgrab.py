import urllib2
from bs4 import BeautifulSoup as bs
import threading
from threading import Lock
import scoregrab

class Gamespot(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url
        
    def run(self):
        lock=threading.Lock()
        count=0
        print "starting",self.url
        page=urllib2.urlopen(self.url).read()
        parser=bs(page)
        a=parser.find("table",{"summary":"GameSpot's All Reviews"})
        game=a.tbody.tr
        while (game):
            title=str(game.th.a.contents[0])
            platform=a.tbody.td.span.contents[0]
            scoreline=a.find("td",{"class":"score"}) 
            home=str(scoreline.a["href"])
            editor_score=str(scoreline.a.contents[0])
            release=a.find("td",{"class":"last"}).contents[0]
            lock.acquire()
            print "\n".join([title, platform, home, editor_score,release]),"\n\n"
            lock.release()
            count+=1
            game=game.nextSibling.nextSibling
        print "\n\n ~~~~~~","Collected data of",count,"games ~~~~~"
        return 1
            
