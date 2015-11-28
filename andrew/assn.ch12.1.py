# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
tags = list()
url = raw_input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_170987.html"
html = urllib.urlopen(url).read()

# print html

soup = BeautifulSoup(html)

# print soup

# Retrieve all of the anchor tags
tags = soup('span')
# print tags

list1 = list()

for tag in tags:
    # Look at the parts of a tag
#     print 'TAG:',tag
#     print 'URL:',tag.get('href', None)
#     print 'Contents:',tag.contents[0]
    numbers = int(tag.contents[0])
    list1.append(numbers)
#     print 'Attrs:',tag.attrs
print sum(list1)
