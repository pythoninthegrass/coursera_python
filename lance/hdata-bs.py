# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html (Sum=2553)
# Actual data:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_166742.html (Sum ends with 12)
# Renamed commit to match assignment

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

nums = []

# Retrieve all of the anchor (a) tags >> subbed span tags
tags = soup('span')
for tag in tags:
   # print 'TAG:',tag
   # print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   # print 'Attrs:',tag.attrs
   nums.append(tag.contents[0])

new_nums = [int(i) for i in nums]

print sum(new_nums)
