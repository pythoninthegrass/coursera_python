# NOTE: Almost had this, but was trying to get without nested for loop. Then looked at Greg's solution at urllinks.py and tweaked the nested for loop into the while loop. 

import urllib
from BeautifulSoup import *

url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Aoibha.html"

list1 = list()
links = 0
n = 0
spot = 0
while n < 7:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    
    for tag in tags:
        spot = spot + 1
        if spot == 18:
            url = tag.get('href', None)
            print url
            spot = 0
            break
    n = n+1

