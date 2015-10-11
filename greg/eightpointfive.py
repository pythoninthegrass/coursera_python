# open mbox-short.txt
# when line starts with
#stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#parse the from using split() and print the email address
#then print out a count at the end

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
lst = []

for line in fh:
	line = line.rstrip()
	if line.startswith("From "):
	    count = count + 1
	    words = line.split()
	    print words[1]
#for line in lst[0:28]


#print lst

print "There were", count, "lines in the file with From as the first word"