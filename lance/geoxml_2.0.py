import urllib
import xml.etree.ElementTree as ET

# url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = ' http://python-data.dr-chuck.net/comments_166739.xml'
uh = urllib.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

count = sum(1 for elem in tree.findall(".//count"))
total = sum(int(c.text) for c in tree.findall('.//count'))

print "Count: ",count
print "Total: ",total