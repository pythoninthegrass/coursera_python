import re

fname = raw_input("Enter file name: ")
# if len(fname) < 1 : fname = "regex-sum.txt"
fh = open(fname)

nums = list()

for line in fh:
    line = line.rstrip()
    y = re.findall(r'\d+', line)
    for item in y:
        try:
            num = int(item)
        except val_error:
            pass
        else:
            nums.append(num)

print sum(nums)

## Original falty solution
# for line in fh:
#     line = line.rstrip()
    # y = re.findall('([0-9]+)', line)
    # if len(y) != 1: continue # original check for integers
    # if len(y) > 0 : continue
    # num = float(y[0])
    # num = int(y[0])
    # nums.append(num)
# print sum(nums)

## Print the hard way -- same results
## Uncomment "sum = 0" on line 8
# for number in nums:
#     sum = sum + number
# print sum