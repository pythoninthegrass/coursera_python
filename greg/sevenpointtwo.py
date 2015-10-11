# open a files and look for this 
# X-DSPAM-Confidence:    0.8475
# count the values from XDspam lines and make value floats
# find average of values
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
container = []
added = 0
average = 0
for line in fh:
	line = line.rstrip()
	if line.startswith('X-DSPAM-Confidence:'):
		count = count + 1
		container.append(float(line[19:]))
for contained in container:
	added = contained + added
	average = added / count
print "Average spam confidence:", average
