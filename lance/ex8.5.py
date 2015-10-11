# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

email = []

for line in fh:
    if line.startswith("From:"):
        line = line.strip()
        words = line.split() # useless with for function below
        email.append(line[6:])
        
for line in email: print line # best solution but playground wants split() too
# print("\n".join(email)) # does same as for line above, left for ref

count = sum(1 for line in email)

print "There were", count, "lines in the file with From as the first word"