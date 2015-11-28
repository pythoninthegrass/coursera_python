#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent #the greatest number of mail messages. The program looks for 'From ' lines and takes the #second word of those lines as the person who sent the mail. The program creates a Python #dictionary that maps the sender's mail address to a count of the number of times they #appear in the file. After the dictionary is produced, the program reads through the #dictionary using a maximum loop to find the most prolific committer.

#create file handle
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#create dictionary to input email addresses, count of each time seen
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    emails = words[1]
    #print emails
    counts[emails] = counts.get(emails,0)+1
#print counts

#find most frequent email address seen and number of times seen
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount