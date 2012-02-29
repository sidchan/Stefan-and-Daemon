import urllib2
from bs4 import BeautifulSoup as bs
import threading
import scoregrab
import linkgrab
import metacritic

GRABSITES=[]
LINKSITES=["http://asia.gamespot.com/reviews.html?mode=all&page="+str(i) for i in range(10)]
GRABCOUNT=0
LINKCOUNT=0
running=0

def main():
    global LINKSITES, LINKCOUNT, running
    running=1
    while LINKSITES or running:
        for link in LINKSITES:
            LINKSITES.remove(link)
            if LINKCOUNT<10:
                if "gamespot" in link:
                    linkgrab.Gamespot(link).start()
                    LINKCOUNT+=1
                if "metacritic" in link:
                    metacritic.Metacritic(link).start()
                
        
                else:
                    time.sleep(0.1)


#def main():
    #while WEBSITES:
        #if COUNT<6:
            #for site in WEBSITES:
                #if "gamespot" in site:
                    #print Gamespot(site).start()
        #else:
            #time.sleep(0.1)
    #print "done"

        

if __name__=="__main__":
    main()