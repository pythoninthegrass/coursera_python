#open romeo.txt
#split lines into a list of words
#Check to see if word is in list if it is not then add the word
#sort the list and print list in alphabetical order

fname = raw_input("Enter a file name: ")
fh = open(fname)
lst = []

def remove_duplicates(l):
    return list(set(l))

for line in fh:
	line = line.rstrip()
	lst.append(line)
a = lst[0]
b = lst[1]
c = lst[2]
d = lst[3]

aa = a.split()
bb = b.split()
cc = c.split()
dd = d.split()

word = aa + bb + cc + dd
huh = remove_duplicates(word)

print sorted(huh)


