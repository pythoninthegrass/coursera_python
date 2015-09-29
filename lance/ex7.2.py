# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # print line # displays whole line
    # print line # displays X-DSPAM-Confidence: 0...
    # print line[0:18] # displays X-DSPAM-Confidence:
    # print line[20:] # displays 0...
    line_num = line[20:] # stores 0...
    
value = float(line_num)
total = total + value
count = count + 1

average = total / count
print "Average spam confidence:",average


# for var in fh:
#     count = count + 1
#     print count

# print line.find('0.')

# slice = line[::27]
# print slice

#print line

# avg = sum(conf_num,0.0) / len(conf_num)
    # print "The average of {0} numbers is {1}".format(len(conf_num),avg)