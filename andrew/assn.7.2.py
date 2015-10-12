#7.2 Write a program that prompts for a file name, then opens that file and reads through #the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and #compute the average of those values and produce an output as shown below.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when #you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
    
#read through file for specific lines and count total
count = 0
#create blank list to append specific lines
mylist = []
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    mylist.append(float(line[20:]))
    #calculate average of extracted numbers
    avglist = sum(mylist)/len(mylist)

print 'Average spam confidence:',avglist

#below is previous code to locate parse lines related to the line[20:] above

# mylist2 = str(mylist)
# mylist3 = float(mylist2)
# print mylist

#print 'Line Count:', count

#print mylist

#convert mylist to floating point values
#mylistnum = float(mylist)

#mylist2 = str(mylist)
#atpos = mylist2.find('0.')
#print type(mylist2)
#print atpos
#sppos = mylist2.find('5',atpos)
#print sppos
#host = mylist2[atpos:sppos+1]
#host2 = float(host)

#print type(host2)
#print host2


print "Done"