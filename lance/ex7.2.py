# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print line

#line.find('0.', 27)
#print line

# avg = sum(conf_num,0.0) / len(conf_num)
    # print "The average of {0} numbers is {1}".format(len(conf_num),avg)