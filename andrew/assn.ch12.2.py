import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1 : url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Aoibha.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# print soup

list1 = list()
tags = soup('a')

# print tags
for tag in tags:
#     print tag.get('href', None)
    links = tag.get('href', None)
    list1.append(links)
#     for link[18] in links:
# print list1[17]

newurl2 = urllib.urlopen(list1[17]).read()
soup2 = BeautifulSoup(newurl2)

list2 = list()
tags2 = soup2('a')

for tag in tags2:
    links2 = tag.get('href',None)
    list2.append(links2)
# print list2[18]

newurl3 = urllib.urlopen(list2[17]).read()
soup3 = BeautifulSoup(newurl3)

list3 = list()
tags3 = soup3('a')

for tag in tags3:
    links3 = tag.get('href',None)
    list3.append(links3)
# print list3[18]

newurl4 = urllib.urlopen(list3[17]).read()
soup4 = BeautifulSoup(newurl4)

list4 = list()
tags4 = soup4('a')

for tag in tags4:
    links4 = tag.get('href',None)
    list4.append(links4)
# print list4[18]

newurl5 = urllib.urlopen(list4[17]).read()
soup5 = BeautifulSoup(newurl5)

list5 = list()
tags5 = soup5('a')

for tag in tags5:
    links5 = tag.get('href',None)
    list5.append(links5)
# print list5[18]

newurl6 = urllib.urlopen(list5[17]).read()
soup6 = BeautifulSoup(newurl6)

list6 = list()
tags6 = soup6('a')

for tag in tags6:
    links6 = tag.get('href',None)
    list6.append(links6)
# print list6[18]

newurl7 = urllib.urlopen(list6[17]).read()
soup7 = BeautifulSoup(newurl7)

list7 = list()
tags7 = soup7('a')

for tag in tags7:
    links7 = tag.get('href',None)
    list7.append(links7)
print list7[17]
