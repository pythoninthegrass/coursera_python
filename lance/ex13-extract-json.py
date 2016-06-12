import json
import urllib

# url = 'http://python-data.dr-chuck.net/comments_42.json' # sum = 2482
url = 'http://python-data.dr-chuck.net/comments_42.json'
uh = urllib.urlopen(url)
json_data = uh.read()

# input = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Chuck"
#   }
# ]'''

# info = json.loads(input)
# try:
#     nums = int(json_data)
# except:
#     nums = -1 # impossible age but valid int fallback
# info = json.loads(nums)
info = json.loads(json_data)

# count = sum(1 for x in info(".//comments"))

print 'User count:', len(count)

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
