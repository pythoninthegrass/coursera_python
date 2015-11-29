# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
#Last name in sequence: Anayah
# Actual data:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_166742.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: D
import urllib
from BeautifulSoup import *

# address = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
address = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Jaksyn.html'

# Number of repeated processes
n = 0

# Position counter
x = 0

## address1 (AKA sample problem)
# while n < 4:
#
#     html = urllib.urlopen(address).read()
#     soup = BeautifulSoup(html)
#     tags = soup('a')
#
#     for link in tags:
#         x = x + 1
#         if x == 3:
#             address = link.get('href', None)
#             print address
#             x = 0
#             break
#     n = n + 1

## address2 (AKA actual problem)
while n < 7:
    html = urllib.urlopen(address).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for link in tags:
        x = x + 1
        if x == 18:
            address = link.get('href', None)
            print address
            x = 0
            break
    n = n + 1