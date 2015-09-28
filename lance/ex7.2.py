# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line

count = 0

for var in fh:
    count = count + 1
    print count

# print line.find('0.')

# slice = line[::27]
# print slice

#print line

# avg = sum(conf_num,0.0) / len(conf_num)
    # print "The average of {0} numbers is {1}".format(len(conf_num),avg)