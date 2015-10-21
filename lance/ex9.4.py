#mbox-short.
fname = raw_input("Enter file: ")
fh = open(fname)

counts = dict()

for line in fh:
    if line.startswith("From:"):
        words = line.split()
        words.remove("From:")
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

print counts

maxval = None
maxkee = None

for kee,val in counts.items():
    if maxval == None or maxval < val :
        maxval = val
        maxkee = kee

print maxkee, maxval