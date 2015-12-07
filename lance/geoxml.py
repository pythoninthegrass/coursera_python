import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_42.xml'

while True:
    # address = raw_input('Enter location: ')
    # if len(address) < 1 : break

    # print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)
    count = tree.findall('.//count')
    print count