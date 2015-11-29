import urllib
import xml.etree.ElementTree as ET

count = 0
lst = []

fhand = raw_input("Please input a url. ")
if len(fhand) == 0:
    fhand = 'http://python-data.dr-chuck.net/comments_167521.xml'

thing = urllib.urlopen(fhand).read()
root = ET.fromstring(thing)
line = root.findall(".//count")

count = len(line)

for child in line:
    lst.append(int(child.text))

print count
print sum(lst)
