fname = raw_input("Enter file: ")
fh = open(fname)
# text = fh.read() # Causes empty "{}" 

counts = dict()

for line in fh:
    if line.startswith("From:"):
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

print counts

## Shorthand get function that does the for loop above
# for word in words:
#     counts[word] = counts.get(word,0) + 1

# print counts.items()


## Video Solution - Needs to exclude "From: 27"
maxval = None
maxkee = None

for kee,val in counts.items():
    if maxval == None or maxval < val :
        maxval = val
        maxkee = kee
    # print kee, val, maxval, maxkee

print maxkee, maxval


## Forums Solution - Needs to exclude "From: 27"
# import operator

# highkey=max(counts.items(), key=operator.itemgetter(1))[0]

# print highkey, counts[highkey]