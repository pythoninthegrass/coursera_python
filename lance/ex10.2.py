#Figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and 
#then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the 
#counts, sorted by hour as shown below.
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counts = dict()

for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()

for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)

for val, key in lst[:10]:
    print key, val

## original code
# counts = dict()

# for line in fh:
#     if line.startswith("From:"):
#         words = line.split()
#         words.remove("From:")
#         for word in words:
#             if word not in counts:
#                 counts[word] = 1
#             else:
#                 counts[word] += 1

# print counts
