# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

numlist = list()
for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # print line # displays whole line
    # print line # displays X-DSPAM-Confidence: 0...
    # print line[0:18] # displays X-DSPAM-Confidence:
    # print line[20:] # displays 0...
    # line_num = line[20:] # stores 0...
    line_num = line.split(":")
    # print line_num[1]
    value = float(line_num)
    numlist.append(value)

## Second Average List
# value = float(line_num)
average = sum(numlist) / len(numlist)
print "Average spam confidence:",average

## Original Average List
# total = 0
# count = 0

# email = line_num[1]
# total = total + email
# # total = total + value
# count = count + 1

# average = total / count
# print "Average spam confidence:",average


## Detritus
# for var in fh:
#     count = count + 1
#     print count

# print line.find('0.')

# slice = line[::27]
# print slice

#print line

# avg = sum(conf_num,0.0) / len(conf_num)
    # print "The average of {0} numbers is {1}".format(len(conf_num),avg)