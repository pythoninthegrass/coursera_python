# open a files and look for this 
# X-DSPAM-Confidence:    0.8475
# count the values from XDspam lines and make value floats
# find average of values
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

total = 0
count = 0
nums = []

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
    	line = line.strip()
    	nums.append(line[20:])

new_nums = [float(i) for i in nums]

average = sum(new_nums) / len(new_nums)
print "Average spam confidence:",average