#Figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and 
#then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the 
#counts, sorted by hour as shown below.
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

email = []

for line in fh:
    if line.startswith("From:"):
        line = line.strip()
        words = line.split()
        # email.append(line[6:])
    

# for line in email: print line # best solution but playground wants split() too
# print("\n".join(email)) # does same as for line above, left for ref

# count = sum(1 for line in email)

# print "There were", count, "lines in the file with From as the first word"