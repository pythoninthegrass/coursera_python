#NOTE: Import regular expression library and open file
mport re
name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_170982.txt"
handle = open(name)

# create list
numlist = list()

#NOTE: extract all numbers in file using regular expressions, and append into empty list
for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) < 1 : continue
    for string in numbers:
#NOTEthis was incorrect nested for loop, just need to append individual numbers into list without creating a "List of Lists"
#         value = int(string[0])
#         valuesum = sum(value)
#     num = int(numbers[0])
        numlist.append(string)

# print numlist


#NOTE: create 2nd empty list, convert to integers, 
intlist = list()
for item in numlist:
    value = int(item)
    intlist.append(value)

# print intlist
print sum(intlist)