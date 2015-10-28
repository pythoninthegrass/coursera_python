import re

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum.txt"
fh = open(fname)

nums = list()

for line in fh:
    line = line.rstrip()
    y = re.findall('([0-9]+)', line)
    if len(y) != 1: continue
    num = float(y[0])
    nums.append(num)

print nums