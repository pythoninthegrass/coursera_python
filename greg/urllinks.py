import urllib
from BeautifulSoup import *

count = 0
position = 0

url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Forrest.html'

while count != 7:

    html = urllib.urlopen(url)
    data = html.read()
    soup = BeautifulSoup(data)
    tags = soup('a')

    for tag in tags:
    	position = position + 1
    	if position == 18:
            url = tag.get('href', None)
            print url
            count = count + 1
            position = 0
            break
    continue
