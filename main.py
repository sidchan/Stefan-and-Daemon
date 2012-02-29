import urllib2
from bs4 import BeautifulSoup as bs
import thread
import scoregrab
import linkgrab

GRABSITES=[]
LINKSITES=[]
GRABCOUNT=0
LINKCOUNT=0


def main():
    while LINKSITES:
        if LINKCOUNT<10:
            if "gamespot" in link:
                linkgrab.Gamespot(link).start()
                LINKCOUNT+=1
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