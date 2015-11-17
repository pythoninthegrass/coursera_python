# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
#Last name in sequence: Anayah
# Actual data:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_166742.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: D

import urllib
from BeautifulSoup import *

# url = raw_input('Enter URL: ')
url = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html').read()
# html = urllib.urlopen(url).read()

# soup = BeautifulSoup(html)
soup = BeautifulSoup(url)

# Retrieve all of the anchor (a) tags
tags = soup('a')

# links = []

for tag in tags:
   # print tag.get('href', None)
   # results = tag.get('href', None)
   # count = raw_input('Enter count: ') # fetch count
   # position = raw_input('Enter position: ') # fetch position
   # tags[position].get('href', None)
   print tags[17].get('href', None)
   # words = results.split()
   # links.append(words[0:])
   # print links