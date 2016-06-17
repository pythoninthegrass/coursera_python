import json
import urllib

# url = 'http://python-data.dr-chuck.net/comments_42.json' # sum = 2553
url = 'http://python-data.dr-chuck.net/comments_166743.json'
uh = urllib.urlopen(url).read()

info = json.loads(uh)

nums = [] # list
numbers = 0 # counter

for item in info['comments']:
    nums.append(item['count'])
    numbers = numbers + item['count']
    # print numbers # shows iteration adding up to 2553

print "The number of items counted is: ",len(nums)
print "These are the numbers: ",nums
print "The sum of counted numbers is: ",numbers
