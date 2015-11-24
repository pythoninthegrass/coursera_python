import urllib
from BeautifulSoup import *
import re

yum = []
url = 'http://python-data.dr-chuck.net/comments_167524.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')
for tag in tags:
	#tag = re.search(str(tag), [0-9]) 
	yum.append(tag.contents[0])

#for things in yum:
	#things.split(0-3)

print yum
