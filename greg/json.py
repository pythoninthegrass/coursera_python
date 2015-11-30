import json
import urllib

add = 0

url = 'http://python-data.dr-chuck.net/comments_167525.json'
raw = urllib.urlopen(url).read()

info = json.loads(raw)

for item in info['comments']:
    add = add + item['count']

print add
