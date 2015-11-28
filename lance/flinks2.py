# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
#Last name in sequence: Anayah
# Actual data:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_166742.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: D
import urllib
from BeautifulSoup import *

address1 = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
address2 = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Jaksyn.html'

# Number of repeated processes
n = 0

# Position counter
x = 0

#pos = raw_input('Enter Position: ')

while n < 4:
#    print 'Retrieving URL'
    html = urllib.urlopen(address2).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
#    link = tag.get('href', None)
    for link in tags:
        x = x + 1
        if x == 3:
            address = link.get('href', None)
            print address
            x = 0
            break
    n = n + 1