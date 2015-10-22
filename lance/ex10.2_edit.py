#Figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and 
#then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the 
#counts, sorted by hour as shown below.
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

lst = []

for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()[5]
        lst.append(words[:2])

<<<<<<< HEAD

counts = dict()

=======
# lst.sort(reverse=True)

# print lst

counts = dict()

>>>>>>> c4fd0a6e57bf0a786fa60dd26b25b7791db2e1c5
for line in lst:
    counts[line] = counts.get(line, 0) + 1

# print counts.items()

<<<<<<< HEAD
for k, v in sorted(counts.items()):
    print k, v
=======
for k, v in counts.items():
    # lst.append((k, v))
    print (k, v)
>>>>>>> c4fd0a6e57bf0a786fa60dd26b25b7791db2e1c5

## Nicer output than for loop above. Still not the correct format.
# import pprint
# pprint.pprint(counts)